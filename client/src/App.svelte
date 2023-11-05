<script lang="ts">
  import MainForm from './components/MainForm.svelte'

  async function callOpenAI() {
    const response = await fetch('/api/openai-call', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({}),
    })
    const data = await response.json()
    console.log(data.result) // Handle the API response as needed
  }
</script>

<main>
  <div class="container">
    <!-- <button on:click={callOpenAI}>Call OpenAI</button> -->

    <MainForm />
  </div>
</main>

<style>
  main {
    padding: 0;
  }
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>
