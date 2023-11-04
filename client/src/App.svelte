<script lang="ts">
  export let name: string
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
  </div>
</main>

<style>
  .container {
    margin: 1rem;
    text-align: center;
  }
</style>
