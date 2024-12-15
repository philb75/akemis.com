document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const slides = document.querySelectorAll('.n2-ss-slide-background');
    const totalSlides = slides.length;

    function showSlide(n) {
        // Hide all slides
        slides.forEach(slide => {
            slide.style.opacity = '0';
            slide.style.display = 'none';
        });
        
        // Show and fade in the current slide
        slides[n].style.display = 'block';
        setTimeout(() => {
            slides[n].style.opacity = '1';
        }, 10);
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }

    // Add transition styles to slides
    slides.forEach(slide => {
        slide.style.transition = 'opacity 0.5s ease-in-out';
    });

    // Initialize carousel
    // Show first slide
    showSlide(0);
    
    // Set interval for auto-advance
    setInterval(nextSlide, 5000);
});
