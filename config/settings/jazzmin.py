"""
Jazzmin configuration for Django admin interface
"""

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "AlumniVerse Admin",
    # Title on the login screen (19 chars max) (Will default to current_admin_site.site_header if absent or None)
    "site_header": "AlumniVerse",
    # Title on the brand (19 chars max) (Will default to current_admin_site.site_header if absent or None)
    "site_brand": "AlumniVerse",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": None,
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to AlumniVerse",
    # Copyright on the footer
    "copyright": "AlumniVerse Ltd",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "accounts.User",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/S4NKALP/AlumniVerse", "new_window": True},
        {"model": "accounts.User"},
        {"app": "events"},
        {"app": "news"},
        {"app": "jobs"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Custom icons for side menu apps/models
    "icons": {
        "auth": "fas fa-users-cog",
        "accounts.user": "fas fa-user",
        "events": "fas fa-calendar",
        "news": "fas fa-newspaper",
        "jobs": "fas fa-briefcase",
        "forum": "fas fa-comments",
        "mentorship": "fas fa-handshake",
        "achievements": "fas fa-trophy",
        "groups": "fas fa-users",
        "messaging": "fas fa-envelope",
        "notifications": "fas fa-bell",
        "dashboard": "fas fa-tachometer-alt",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS files (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
} 