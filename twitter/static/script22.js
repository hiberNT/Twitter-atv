document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.retweet-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const icon = btn.querySelector('i');
      const countSpan = btn.querySelector('.count');
      let count = parseInt(countSpan.textContent);

      if (icon.classList.contains('retweeted')) {
        icon.classList.remove('retweeted');
        icon.style.color = '';
        countSpan.textContent = count - 1;
      } else {
        icon.classList.add('retweeted');
        icon.style.color = 'rgb(0, 186, 124)';
        countSpan.textContent = count + 1;
      }
    });
  })
  const buttons = document.querySelectorAll('.toggle-comentarios');

  buttons.forEach(button => {
    button.addEventListener('click', function () {
      const postId = this.getAttribute('data-post');
      const box = document.getElementById('comentarios-' + postId);
      const overlay = document.getElementById('overlay-' + postId);

      if (overlay && box) {
        overlay.style.display = 'flex';
        box.style.display = 'block';
      };
    });
  });

  document.querySelectorAll('.overlay').forEach(overlay => {
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) {
        overlay.style.display = 'none';
        const comentariosBox = overlay.querySelector('.comentarios-box');
        if (comentariosBox) comentariosBox.style.display = 'none';
      }
    });
  });

  // Abrir modal ao clicar no ícone de perfil
  document.querySelectorAll('.perfil').forEach(btn => {
    btn.addEventListener('click', () => {
      document.getElementById('perfilModal').style.display = 'block'
    })
  })

  // Fechar modal
  document.querySelector('.close-modal').addEventListener('click', () => {
    document.getElementById('perfilModal').style.display = 'none'
  })

  // Fechar ao clicar fora do modal
  window.addEventListener('click', (e) => {
    const modal = document.getElementById('perfilModal')
    if (e.target === modal) {
      modal.style.display = 'none'
    }
  })

  const imagemInput = document.getElementById('id_imagem');
  const previewImg = document.getElementById('preview-img');

  imagemInput.addEventListener('change', () => {
    const file = imagemInput.files[0];
    if (file) {
      previewImg.src = URL.createObjectURL(file);
    }
  });

});
