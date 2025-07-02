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

});
