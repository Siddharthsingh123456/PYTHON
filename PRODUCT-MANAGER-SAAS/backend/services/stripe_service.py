import os


def create_checkout_session(payload):
    plan = payload.get('plan', 'basic')
    if not os.getenv('STRIPE_SECRET_KEY'):
        return {
            'message': 'stripe key not configured, returning mock session',
            'checkout_url': f'https://example.com/mock-checkout?plan={plan}',
        }, 200

    return {'message': 'implement live Stripe checkout here'}, 501
