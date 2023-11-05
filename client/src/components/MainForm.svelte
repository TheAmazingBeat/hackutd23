<script lang="ts">
  // import Dropzone from 'svelte-file-dropzone/Dropzone.svelte'
  import PopupButton from './PopupButton.svelte'
  let currImage: string, fileInput
  let ageInput: HTMLInputElement,
    zipInput: HTMLInputElement,
    sq_feetInput: HTMLInputElement

  let buttonPressed = false

  function pressFirstButton() {
    buttonPressed = true
  }

  // let files = {
  //   accepted: [],
  //   rejected: [],
  // }

  // function handleFilesSelect(e) {
  //   console.log(e)
  //   const { acceptedFiles, fileRejections } = e.detail
  //   files.accepted = [...files.accepted, ...acceptedFiles]
  //   files.rejected = [...files.rejected, ...fileRejections]
  //   // console.log(files.accepted, files.rejected)

  //   // updates the image preview
  //   let image = files.accepted[files.accepted.length - 1]
  //   let reader = new FileReader()
  //   reader.readAsDataURL(image)
  //   reader.onload = (e) => {
  //     currImage = e.target.result as string
  //   }
  // }

  const onFileSelected = (e) => {
    let image = e.target.files[0]
    let reader = new FileReader()
    reader.readAsDataURL(image)
    reader.onload = (e) => {
      currImage = e.target.result as string
    }
  }

  let location = ' '
</script>

<main>
  <!-- <form action="/api/upload" method="POST" enctype="multipart/form-data"> -->
  {#if currImage}
    <img width="128" src={currImage} alt="Real Estate Property" />
  {:else}
    <img width="128" class="avatar" src="/building_icon.png" alt="" />
  {/if}

  <input
    type="file"
    accept=".jpg, .jpeg, .png"
    name="file"
    on:change={(e) => onFileSelected(e)}
    bind:this={fileInput}
  />

  <!-- <button id="uploadImageArea" type="button" on:click={fileInput.click()}>
      Click to upload images</button
    > -->

  <!-- <Dropzone
      containerClasses={'dropzone'}
      containerStyles={'background:none;'}
      on:drop={handleFilesSelect}
      accept={'.jpg, .jpeg, .png'}
      disableDefaultStyles={true}
      inputElement={fileInput}
    /> -->

  <!-- <div id="otherFieldsContainer">
      <input type="number" placeholder="Age of Property" bind:this={ageInput} />
      <input type="text" placeholder="Zip Code" />
    </div> -->

  <div id="submitContainer">
    <!-- <input type="submit" value="Upload" /> -->
    <button
      on:click={async () => {
        const formData = new FormData()
        formData.append('file', fileInput.files[0])
        pressFirstButton()
        try {
          const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData,
          })

          if (response.ok) {
            // Handle a successful response here
          } else {
            // Handle an error response here
            console.error('Error:', response.statusText)
          }
        } catch (err) {
          console.error('Error:', err)
        }
      }}
    >
      Upload
    </button>
  </div>
  <!-- </form> -->
</main>

<PopupButton />

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
