const themeToggle = document.getElementById("theme-toggle");
const menuToggle = document.getElementById("menu-toggle");
const siteNav = document.getElementById("site-nav");
const revealItems = document.querySelectorAll(".reveal");
const savedTheme = localStorage.getItem("portfolio-theme");

if (savedTheme === "light") {
    document.body.classList.add("light-theme");
}

themeToggle?.addEventListener("click", () => {
    document.body.classList.toggle("light-theme");
    const nextTheme = document.body.classList.contains("light-theme") ? "light" : "dark";
    localStorage.setItem("portfolio-theme", nextTheme);
});

menuToggle?.addEventListener("click", () => {
    siteNav?.classList.toggle("is-open");
});

siteNav?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
        siteNav.classList.remove("is-open");
    });
});

const revealObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                revealObserver.unobserve(entry.target);
            }
        });
    },
    {
        threshold: 0.2,
    }
);

revealItems.forEach((item) => revealObserver.observe(item));

document.querySelector(".contact-form")?.addEventListener("submit", (event) => {
    event.preventDefault();
    const button = event.currentTarget.querySelector("button");
    const originalText = button.textContent;
    button.textContent = "Message Prepared";
    button.disabled = true;

    setTimeout(() => {
        button.textContent = originalText;
        button.disabled = false;
        event.currentTarget.reset();
    }, 1800);
});
