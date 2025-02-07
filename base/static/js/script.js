        // Search functionality
        document.querySelector('.search-icon').addEventListener('click', function(e) {
            e.preventDefault();
            const searchContainer = document.querySelector('.search-container');
            searchContainer.classList.toggle('active');
            if (searchContainer.classList.contains('active')) {
                const searchInput = document.querySelector('.search-input');
                searchInput.focus();
            }
        });

        // Close search when clicking outside
        document.addEventListener('click', function(e) {
            const searchContainer = document.querySelector('.search-container');
            const searchIcon = document.querySelector('.search-icon');
            if (!searchContainer.contains(e.target) && !searchIcon.contains(e.target)) {
                searchContainer.classList.remove('active');
            }
        });

        // Close search when clicking the back button
        document.querySelector('.back-button').addEventListener('click', function() {
            const searchContainer = document.querySelector('.search-container');
            searchContainer.classList.remove('active');
        });