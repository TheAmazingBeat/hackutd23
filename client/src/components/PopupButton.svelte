<script>
  import { isModalOpen, openModal, closeModal } from '../lib/modal'
  let result = ''
  $: result = ''
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

<!-- Button to trigger the modal -->
<button
  class="contrast"
  data-target="modal-example"
  on:click={(e) => {
    callOpenAI(e)
  }}
>
  Call OpenAI
</button>

<!-- Modal -->
<dialog id="modal-example">
  <article>
    <a
      href="#close"
      aria-label="Close"
      class="close"
      data-target="modal-example"
      on:click={(e) => {
        toggleModal(e)
      }}
    />
    <h3>Here is your value proposition:</h3>
    <p>
      {result}
    </p>
    <footer>
      <a
        href="#cancel"
        role="button"
        class="secondary"
        data-target="modal-example"
        on:click={(e) => {
          toggleModal(e)
        }}
      >
        Close
      </a>
    </footer>
  </article>
</dialog>
