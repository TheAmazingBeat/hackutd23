<script lang="ts">
  
    async function callOpenAI() {
          const response = await fetch('/api/openai-call', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({}),
          });
          const data = await response.json();
          console.log(data.result); // Handle the API response as needed
      }
</script>

<main>
  <div class="container">
    <h1>Hello {name}!</h1>
    <form action="/success" method="POST" enctype="multipart/form-data">
      <div id="uploadImageContainer">
        <input type="file" name="file" />
        <input type="submit" value="Upload" />
      </div>

      <div id="otherFieldsContainer">
        <input type="number" />
        <input type="text" />
      </div>
    </form>
  
  <button on:click={callOpenAI}>Call OpenAI</button>
  </div>
</main>

<style>
  .container {
    margin: 1rem;
    text-align: center;
  }
</style>
