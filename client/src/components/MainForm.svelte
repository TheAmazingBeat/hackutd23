<script lang="ts">
  // import Dropzone from 'svelte-file-dropzone/Dropzone.svelte'
  import { append } from 'svelte/internal'
  import { isModalOpen, openModal, closeModal } from '../lib/modal'
  import PopupButton from './PopupButton.svelte'
  import Popup from './Popup.svelte'
  let currImage: string, fileInput
  let ageInput: HTMLInputElement,
    cityInput: HTMLInputElement,
    sq_feetInput: HTMLInputElement

  let result: string = ''

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

  async function callOpenAI(e) {
    const response = await fetch('/api/openai-call', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({}),
    })
    const data = await response.json()
    console.log(data.result) // Handle the API response as needed
    result = data.result
    await toggleModal(e)
  }

  async function toggleModal(event) {
    event.preventDefault()
    const modal = document.getElementById(
      event.target.getAttribute('data-target')
    )
    typeof modal != 'undefined' && modal != null && isModalOpen(modal)
      ? closeModal(modal)
      : openModal(modal)
  }
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

  <input
    type="number"
    min="0"
    name="age"
    bind:this={ageInput}
    placeholder="Age of Property"
  />

  <input
    type="text"
    name="location"
    bind:this={cityInput}
    placeholder="City, State"
  />

  <input
    type="number"
    min="0"
    name="size"
    bind:this={sq_feetInput}
    placeholder="Size in Sqft"
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
      data-target="modal-example"
      on:click={async (e) => {
        const formData = new FormData()
        formData.append('file', fileInput.files[0])
        formData.append('age', ageInput.value)
        formData.append('location', cityInput.value)
        formData.append('size', sq_feetInput.value)
        try {
          const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData,
          })

          if (response.ok) {
            // Handle a successful response here
            callOpenAI(e)
          } else {
            // Handle an error response here
            console.error('Error:', response.statusText)
          }
        } catch (err) {
          console.error('Error:', err)
        }
      }}
    >
      Generate
    </button>
  </div>
  <!-- </form> -->

  <Popup {result} />

  <!-- <PopupButton /> -->
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
