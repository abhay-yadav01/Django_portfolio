document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating input[type="radio"]');
    const message = document.getElementById('feedback-message');

    stars.forEach(star => {
        star.addEventListener('change', () => {
            const value = parseInt(star.value);
            if (value >= 4) {
                message.textContent = '✨ Thanks for your Awesome Feedback!';
            } else {
                message.textContent = '';
            }
        });
    });
});
