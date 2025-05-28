from django.db import models

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(
        "auth.User", 
        verbose_name="Пользователь", 
        on_delete=models.CASCADE,
        related_name='client'
    )
    name = models.TextField("ФИО")
    email = models.TextField("Электронная почта")
    phone = models.TextField("Телефон")
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
    
    def __str__(self) -> str:
        return self.name



class Order(models.Model):
    orderNumber = models.TextField("Номер заказа")
    user = models.ForeignKey("auth.User", verbose_name="Пользователь", on_delete=models.CASCADE, null=True)
    comment = models.TextField("Комментарий")
    date = models.DateField("Дата")
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    def __str__(self) -> str:
        return self.orderNumber


class Vent(models.Model):
    ventName = models.TextField("Название заготовки")
    picture = models.TextField("Изображение")
    class Meta:
        verbose_name = "Заготовка"
        verbose_name_plural = "Заготовки"
    
    def __str__(self) -> str:
        return self.ventName

class List(models.Model):
    orderNumber = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    ventName = models.ForeignKey(Vent, on_delete=models.CASCADE, null=True)
    param = models.TextField("Характеристики")
    quantity = models.TextField("Количество", null=True)
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
    
