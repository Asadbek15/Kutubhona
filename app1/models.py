from django.db import models

class Muallif(models.Model):
    ism=models.CharField(max_length=15)
    tirik=models.BooleanField(default="Tirik")
    yosh=models.PositiveSmallIntegerField()
    kitoblar_soni=models.IntegerField(blank=True)
    def __str__(self):
        return self.ism
    class Meta:
        ordering=("ism",)


class Kitob(models.Model):
    c=(
        ("1","Badiy"),
        ("2","Ilmiy"),
        ("3","Fantastik"),
        ("4","Dokumental"),
        ("5","Tarihiy"),
    )
    nom=models.CharField(max_length=15)
    sana=models.DateField(blank=True)
    sahifa=models.PositiveSmallIntegerField()
    janr=models.CharField(max_length=20,choices=c)
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE,related_name="m_kitoblari")
    def __str__(self):
        return self.nom
    class Meta:
        ordering=("nom",)
class Student(models.Model):
    ism = models.CharField(max_length=15)
    guruh = models.PositiveSmallIntegerField(blank=True)
    kitoblar_soni = models.IntegerField(blank=True, default="0")
    bitiruvchi = models.BooleanField(default=False)

    def __str__(self):
        return self.ism
    class Meta:
        ordering=("ism",)
class Record(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student_record")
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE,related_name="kitoblar_record")
    sana=models.DateTimeField(auto_now_add=True)
    qaytardi=models.CharField(max_length=5,blank=True,default="Yo'q")
    qaytarish_sana=models.DateField(blank=True,null=True)
    def __str__(self):
        return f"{self.student},{self.kitob}"


