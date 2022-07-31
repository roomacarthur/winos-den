
var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);

var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#5f8785'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

card.mount('#card-element', {style: style})