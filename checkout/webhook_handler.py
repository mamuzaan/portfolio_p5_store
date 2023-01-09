from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle a payment_intent_succeeded webhook from Stripe """
        intent = event.data.object
        pid = intent.id
        bag = intent.matadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.country,
                postcode__iexact=shipping_details.postal_code,
                town_or_city__iexact=shipping_details.city,
                street_address1__iexact=shipping_details.line1,
                street_address2__iexact=shipping_details.line2,
                county__iexact=shipping_details.state,
                grand_total=grand_total,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExists:
            for item_id, item_data in json.loads(bag).items():
                try:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=shipping_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.country,
                        postcode=shipping_details.postal_code,
                        town_or_city=shipping_details.city,
                        street_address1=shipping_details.line1,
                        street_address2=shipping_details.line2,
                        county=shipping_details.state,
                    )
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)

        return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle a payment_intent_payment_failed webhook from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
