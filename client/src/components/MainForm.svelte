<script lang="ts">
  import Dropzone from 'svelte-file-dropzone/Dropzone.svelte'
  let currImage: string | ArrayBuffer, fileInput
  let ageInput: HTMLInputElement, zipInput: string

  let files = {
    accepted: [],
    rejected: [],
  }

  function handleFilesSelect(e) {
    const { acceptedFiles, fileRejections } = e.detail
    files.accepted = [...files.accepted, ...acceptedFiles]
    files.rejected = [...files.rejected, ...fileRejections]
    console.log(files.accepted, files.rejected)
  }

  const onFileSelected = (e) => {
    let image = e.target.files[0]
    let reader = new FileReader()
    reader.readAsDataURL(image)
    reader.onload = (e) => {
      currImage = e.target.result
    }
  }
</script>

<main>
  <form action="/success" method="POST" enctype="multipart/form-data">
    <!-- <button
    >
      Upload an image of property
    </button> -->
    {#if currImage}
      <img src={currImage} alt="uploaded image" />
    {:else}
      <img
        width="128"
        class="avatar"
        src="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png"
        alt=""
      />
    {/if}
    <div id="uploadImageContainer">
      <input
        style="display: none"
        type="file"
        accept=".jpg, .jpeg, .png"
        on:change={(e) => onFileSelected(e)}
        name="fileInput"
        bind:this={fileInput}
      />
    </div>

    <Dropzone
      containerClasses={'dropzone'}
      on:drop={handleFilesSelect}
      accept={'.jpg, .jpeg, .png'}
      disableDefaultStyles={true}
    />

    <div id="otherFieldsContainer">
      <input type="number" placeholder="Age of Property" bind:this={ageInput} />
      <input type="text" placeholder="Zip Code" />
    </div>

    <div id="submitContainer">
      <input type="submit" value="Upload" />
    </div>
  </form>
</main>

<style>
  form {
    text-align: center;
  }

  #uploadImageArea {
    background: none;
    color: #ddd;
    border: 0.25rem dashed #ddd;
    border-radius: 5px;
    width: 100%;
    height: 5rem;
    cursor: pointer;
  }

  .dropzone {
    background: none;
    color: #ddd;
    border: 0.25rem dashed #ddd;
    border-radius: 5px;
    width: 100%;
    height: 5rem;
    cursor: pointer;
    text-align: center;
  }
</style>
