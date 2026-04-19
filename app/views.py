from django.shortcuts import render


def home(request):
    projects = [
        {
            "title": "Campus Event Hub",
            "description": "A responsive event discovery platform with streamlined browsing, RSVP flows, and admin-friendly content updates.",
            "stack": ["Django", "PostgreSQL", "Bootstrap"],
            "link": "#",
        },
        {
            "title": "Insight Dashboard",
            "description": "A modern analytics experience that turns reporting data into clean, actionable charts for growing teams.",
            "stack": ["JavaScript", "Chart.js", "REST API"],
            "link": "#",
        },
        {
            "title": "Creative Storefront",
            "description": "An ecommerce landing experience focused on polished storytelling, mobile performance, and conversion-minded UX.",
            "stack": ["HTML", "CSS", "JavaScript"],
            "link": "#",
        },
    ]

    skills = [
        "HTML5",
        "CSS3",
        "JavaScript",
        "Python",
        "Django",
        "Responsive Design",
        "UI/UX Thinking",
        "Git & GitHub",
        "REST APIs",
        "SQL",
    ]

    context = {
        "name": "Imanishimwe Gilbert",
        "title": "Frontend-Focused Web Developer",
        "intro": (
            "I build elegant, responsive digital experiences with a sharp eye for layout, motion, "
            "and maintainable code."
        ),
        "about": (
            "I'm a developer who enjoys crafting websites that feel modern, intuitive, and full of "
            "personality. I care about clean code, strong visual hierarchy, and interfaces that work "
            "beautifully across devices."
        ),
        "skills": skills,
        "projects": projects,
        "email": "gilbert@example.com",
        "location": "Kigali, Rwanda",
    }
    return render(request, "index.html", context)
