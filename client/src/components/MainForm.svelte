<script lang="ts">
  import Dropzone from 'svelte-file-dropzone/Dropzone.svelte'
  import PopupButton from './PopupButton.svelte'
  let currImage: string, fileInput
  let ageInput: HTMLInputElement, zipInput: string

  let files = {
    accepted: [],
    rejected: [],
  }

  function handleFilesSelect(e) {
    const { acceptedFiles, fileRejections } = e.detail
    files.accepted = [...files.accepted, ...acceptedFiles]
    files.rejected = [...files.rejected, ...fileRejections]
    // console.log(files.accepted, files.rejected)

    // updates the image preview
    let image = files.accepted[files.accepted.length - 1]
    let reader = new FileReader()
    reader.readAsDataURL(image)
    reader.onload = (e) => {
      currImage = e.target.result as string
    }
  }
</script>

<PopupButton />

<main>
  <form action="/api/upload" method="POST" enctype="multipart/form-data">
    {#if currImage}
      <img width="128" src={currImage} alt="Real Estate Property" />
    {:else}
      <img width="128" class="avatar" src="/building_icon.png" alt="" />
    {/if}

    <Dropzone
      containerClasses={'dropzone'}
      containerStyles={'background:none;'}
      on:drop={handleFilesSelect}
      accept={'.jpg, .jpeg, .png'}
      disableDefaultStyles={true}
      inputElement={fileInput}
    />

    <!-- <div id="otherFieldsContainer">
      <input type="number" placeholder="Age of Property" bind:this={ageInput} />
      <input type="text" placeholder="Zip Code" />
    </div> -->

    <div id="submitContainer">
      <input type="submit" value="Upload" />
    </div>
  </form>
</main>

<style>
  form {
    text-align: center;
  }

  .dropzone {
    /* background: none !important;
    color: #333 !important; */
    border: 0.25rem dashed #ddd;
    border-radius: 5px;
    width: 100%;
    height: 5rem;
    cursor: pointer;
    text-align: center;
  }
</style>
