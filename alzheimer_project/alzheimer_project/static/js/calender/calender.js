// script.js

const months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];
  
  const weekdays = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
  
  const today = new Date();
  let currentMonth = today.getMonth();
  let currentYear = today.getFullYear();
  
  document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;
  
  document.getElementById("prevButton").addEventListener("click", () => {
    currentMonth -= 1;
    if (currentMonth < 0) {
      currentMonth = 11;
      currentYear -= 1;
    }
    document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;
    renderCalendar();
  });
  
  document.getElementById("nextButton").addEventListener("click", () => {
    currentMonth += 1;
    if (currentMonth > 11) {
      currentMonth = 0;
      currentYear += 1;
    }
    document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;
    renderCalendar();
  });
  
  function renderCalendar() {
    const calendarDays = document.getElementById("calendarDays");
    calendarDays.innerHTML = "";
  
    const firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
  
    for (let i = 0; i < firstDayOfMonth; i++) {
      const emptyDay = document.createElement("div");
      calendarDays.appendChild(emptyDay);
    }
  
    for (let i = 1; i <= daysInMonth; i++) {
      const day = document.createElement("div");
      day.innerText = i;
      calendarDays.appendChild(day);
    }
  }
  
  renderCalendar();

  