from django.shortcuts import render


def home(request):
    projects = [
        {
            "title": "Campus Event Hub",
            "description": "A responsive event discovery platform with streamlined browsing, RSVP flows, and admin-friendly content updates.",
            "stack": ["Django", "PostgreSQL", "Bootstrap"],
            "link": "https://github.com/ManGilbert",
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
        "name": "Gilbert Imanishimwe",
        "title": "Full Stack Developer",
        "intro": (
            "I am a passionate Full Stack Developer creating innovative web solutions with modern technologies."
        ),
        "about": (
            "As a Full Stack Developer based in Kigali Nyarugenge, I specialize in building modern, responsive web applications. "
            "I have experience in various technologies and love turning ideas into reality through clean, efficient code."
        ),
        "skills": skills,
        "projects": projects,
        "email": "imanishimwe.glbrt@gmail.com",
        "location": "Kigali Nyarugenge",
    }
    return render(request, "index.html", context)
