document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("scanForm");
  const loader = document.getElementById("loader");
  const submitBtn = document.getElementById("submitBtn");

  if (form) {
    form.addEventListener("submit", () => {
      if (loader) loader.style.display = "block";
      if (submitBtn) {
        submitBtn.style.opacity = "0.7";
        submitBtn.style.pointerEvents = "none";
        submitBtn.innerText = "Scanning...";
      }
    });
  }
});
