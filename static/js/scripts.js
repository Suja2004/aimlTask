function analyzeText() {
  const text = document.getElementById("text").value;
  const sentenceCount = document.getElementById("sentenceCount").value; //sentence count

  fetch('/summarize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text: text, sentence_count: sentenceCount }) 
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("result").innerText = data.summary;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function toggleAdvancedOptions() {
  const advancedOptions = document.getElementById("advancedOptions");
  if (advancedOptions.style.display === "none") {
    advancedOptions.style.display = "flex";
  } else {
    advancedOptions.style.display = "none"; 
  }
}
