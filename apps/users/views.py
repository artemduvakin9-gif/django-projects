from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')

    return render(request, 'users/pages/register.html', {'form': form})
