// static/js/script.js

// Snowflakes animation
document.addEventListener("DOMContentLoaded", function() {
    var snowflakes = document.querySelectorAll('.snowflake');
    snowflakes.forEach(function(snowflake) {
        snowflake.style.animationDuration = Math.random() * (15 - 10) + 10 + 's';
        snowflake.style.animationDelay = Math.random() * (5 - 0) + 's';
    });
});
