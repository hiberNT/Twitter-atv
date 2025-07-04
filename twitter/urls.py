from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import traceback

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            repo = git.Repo('/home/Hibernon/Twitter-atv')
            origin = repo.remotes.origin
            pull_result = origin.pull()
            return HttpResponse(f"✅ Pull feito com sucesso: {pull_result}")
        except Exception as e:
            return HttpResponse(f"❌ Erro ao fazer pull: {str(e)}\n\n{traceback.format_exc()}")
    return HttpResponse("❌ Método inválido. Use POST.")
