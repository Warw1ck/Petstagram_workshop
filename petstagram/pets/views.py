from django.shortcuts import render, redirect

# Create your views here.
from petstagram.pets.forms import PetForm, DeletePetForm
from petstagram.pets.models import Pet


def pet_detail(request, username, slug):
    pet = Pet.objects.get(slug=slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context ={
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {'form': form}
    return render(request, 'pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('home page')
    form = DeletePetForm(initial=pet.__dict__)


    context = {'form': form}
    return render(request, 'pets/pet-delete-page.html', context=context)