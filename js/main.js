/**
 * CWB Topografia - Main JavaScript
 * Desde 2020
 */

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavigation();
    initSmoothScroll();
    initScrollAnimations();
    initContactForm();
    initScrollHeader();
});

/**
 * Mobile Navigation Toggle
 */
function initNavigation() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
}

/**
 * Smooth Scroll for Navigation Links
 */
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(function(link) {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);

                if (target) {
                    const headerHeight = document.querySelector('.header').offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

/**
 * Header Scroll Effect
 */
function initScrollHeader() {
    const header = document.querySelector('.header');

    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 100) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // Update active nav link based on scroll position
    updateActiveNavLink();
    window.addEventListener('scroll', updateActiveNavLink);
}

/**
 * Update Active Navigation Link
 */
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    const headerHeight = document.querySelector('.header').offsetHeight;

    let currentSection = '';

    sections.forEach(function(section) {
        const sectionTop = section.offsetTop - headerHeight - 100;
        const sectionHeight = section.offsetHeight;

        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
        }
    });

    navLinks.forEach(function(link) {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentSection) {
            link.classList.add('active');
        }
    });
}

/**
 * Scroll Animations (Intersection Observer)
 */
function initScrollAnimations() {
    // Elements to animate
    const animatedElements = document.querySelectorAll(
        '.servico-card, .projeto-card, .membro-card, .sobre-content, .contato-item'
    );

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        animatedElements.forEach(function(element) {
            element.style.opacity = '0';
            observer.observe(element);
        });
    } else {
        // Fallback for browsers without IntersectionObserver
        animatedElements.forEach(function(element) {
            element.classList.add('fade-in-up');
        });
    }
}

/**
 * Contact Form Handler
 */
function initContactForm() {
    const form = document.getElementById('contato-form');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(form);
            const data = {};
            formData.forEach(function(value, key) {
                data[key] = value;
            });

            // Basic validation
            if (!data.nome || !data.email || !data.servico || !data.mensagem) {
                showNotification('Por favor, preencha todos os campos obrigatórios.', 'error');
                return;
            }

            // Email validation
            if (!isValidEmail(data.email)) {
                showNotification('Por favor, insira um e-mail válido.', 'error');
                return;
            }

            // Here you would typically send the data to a server
            // For now, we'll just show a success message
            console.log('Form data:', data);

            // Show success message
            showNotification('Mensagem enviada com sucesso! Entraremos em contato em breve.', 'success');

            // Reset form
            form.reset();
        });
    }
}

/**
 * Email Validation
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Show Notification
 */
function showNotification(message, type) {
    // Remove existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'notification notification-' + type;
    notification.innerHTML = '\n        <span class="notification-message">' + message + '</span>\n        <button class="notification-close">&times;</button>\n    ';

    // Add styles
    notification.style.cssText = '\n        position: fixed;\n        top: 100px;\n        right: 20px;\n        padding: 16px 24px;\n        border-radius: 8px;\n        background-color: ' + (type === 'success' ? '#2E7D32' : '#c62828') + ';\n        color: white;\n        font-family: "Open Sans", sans-serif;\n        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);\n        z-index: 9999;\n        display: flex;\n        align-items: center;\n        gap: 12px;\n        animation: slideIn 0.3s ease;\n    ';

    // Add animation keyframes
    const style = document.createElement('style');
    style.textContent = '\n        @keyframes slideIn {\n            from {\n                transform: translateX(100%);\n                opacity: 0;\n            }\n            to {\n                transform: translateX(0);\n                opacity: 1;\n            }\n        }\n    ';
    document.head.appendChild(style);

    // Close button style
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.style.cssText = '\n        background: none;\n        border: none;\n        color: white;\n        font-size: 20px;\n        cursor: pointer;\n        padding: 0;\n        line-height: 1;\n    ';

    // Add to DOM
    document.body.appendChild(notification);

    // Close button functionality
    closeBtn.addEventListener('click', function() {
        notification.remove();
    });

    // Auto remove after 5 seconds
    setTimeout(function() {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

/**
 * Lazy Load Images (optional enhancement)
 */
function initLazyLoad() {
    const images = document.querySelectorAll('img[data-src]');

    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(function(img) {
            imageObserver.observe(img);
        });
    } else {
        // Fallback
        images.forEach(function(img) {
            img.src = img.dataset.src;
        });
    }
}

/**
 * Counter Animation for Stats (optional)
 */
function animateCounter(element, target, duration) {
    let start = 0;
    const increment = target / (duration / 16);

    function updateCounter() {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start) + '+';
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target + '+';
        }
    }

    updateCounter();
}
