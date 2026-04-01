  // adding functionality to the send input button

document.querySelector(".js-send-input-button").addEventListener('click', () => {

    const input = document.querySelector('.js-input');
    const value = input.value;
    const container = document.querySelector('.js-message-body');
    

    if(value === '') {
        document.querySelector('.js-message-body').innerHTML += 
        `<p>Please enter a message!</p>`
      } else {
        document.querySelector('.js-message-body').innerHTML += `
          <div class="sent">${value}</div>`
        input.value = '';
        

       
        const message = {
          message: value,
        }
        console.log(message);

        fetch('/api/chats', {
          method: 'POST',

          headers: {
             'Content-Type': 'application/json'
              },

          body: JSON.stringify(message)

        }).then(response => response.json())
        .then(data => {
          document.querySelector('.js-message-body').innerHTML += `
          <div class="response">${data.message}</div>`
        })
        
      }
})  

// adding functionality to the clear input button

document.querySelector('.js-clear-input-button').addEventListener('click', () => {

    const input = document.querySelector('.js-input');
    const value = input.value;

    if(input.value !== '') {
        input.value = '';
    }
})

