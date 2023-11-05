<script>
  import { isModalOpen, openModal, closeModal } from '../lib/modal'
  export let result = ''
  $: result = ''

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

<style>
article{
  text-align: left !important;
}
</style>