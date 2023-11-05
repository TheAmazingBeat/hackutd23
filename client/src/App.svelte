<script lang="ts">
  import MainForm from './components/MainForm.svelte'
</script>

<main>
  <div class="container">
    <MainForm />
  </div>
</main>

<style>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>
