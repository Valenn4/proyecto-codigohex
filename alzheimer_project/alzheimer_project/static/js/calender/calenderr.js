// script.js

const formAction = document.querySelector(".formAction")
const formObject = document.querySelector(".formObject")
const formGame = document.querySelector(".formGame")
const formMusic = document.querySelector(".formMusic")

formObject.style.display = 'none'
formMusic.style.display = 'none'
formGame.style.display = 'none'

function clickOption(option){
  switch(option){
    case 'action':
      formAction.style.display = 'block'
      formObject.style.display = 'none'
      formGame.style.display = 'none'
      formMusic.style.display = 'none'
      break;
    case 'object':
      formAction.style.display = 'none'
      formObject.style.display = 'block'
      formGame.style.display = 'none'
      formMusic.style.display = 'none'
      break;
    case 'game':
      formAction.style.display = 'none'
      formObject.style.display = 'none'
      formGame.style.display = 'block'
      formMusic.style.display = 'none'
      break;
    case 'music':
      formAction.style.display = 'none'
      formObject.style.display = 'none'
      formGame.style.display = 'none'
      formMusic.style.display = 'block'
      break;
  }
}
  

const months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];
  
  const weekdays = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
  
  const today = new Date();
  let currentMonth = today.getMonth();
  let currentYear = today.getFullYear();
  
  document.getElementById("monthYear").innerText = `${months[currentMonth]} ${currentYear}`;
  
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
      
      fetch(`http://127.0.0.1:8000/api/activities/${document.getElementById("id_user").innerHTML}/${currentYear}/${currentMonth+1}/${i}`)
      .then(response => response.json())
      .then(json => {
        let activity = ''
        
        if(json.length>0){
          day.insertAdjacentHTML("beforeend", `<p>${i}</p>`)
          for(a of json){
            if(a.id_action!=null){
              activity = a.id_action
            } else if(a.id_music!=null){
              activity = a.id_music
            } else if(a.id_game!=null){
              activity = a.id_game
            } else if(a.id_object!=null){
              activity = a.id_object
            }
            day.insertAdjacentHTML("beforeend", `<p>${a.time}${activity.name}</p>`)

          }
        } else {
          day.insertAdjacentHTML("beforeend", `<p>${i}</p>`)
        }
      })
      calendarDays.appendChild(day);

    }
  }
  
  renderCalendar();

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

