from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=12, null=False, blank=False, choices=[('client', 'client'),
                                                                              ('manager', 'manager'),
                                                                              ('expert', 'expert')])
    def __str__(self):
        return self.title

class Profile(models.Model):
    firstname = models.CharField(max_length=25 )
    lastname = models.CharField(max_length=50 )
    username = models.CharField(max_length=25 )
    password = models.CharField(max_length=50 )
    phone = models.CharField(max_length=50)
    national_code = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    refer_code = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname +" "+ self.lastname} --- {self.role}'


class sell_Property(models.Model):
    owner = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    meterage = models.CharField(max_length=10)
    construction_year = models.CharField(max_length=10)
    neighborhood_name = models.CharField(max_length=50)
    parking = models.BooleanField(null=False)
    sell_price = models.PositiveIntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.neighborhood_name} --- {self.owner} --- {self.sell_price} '

class rent_Property(models.Model):
    owner = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    meterage = models.CharField(max_length=10)
    construction_year = models.CharField(max_length=10)
    neighborhood_name = models.CharField(max_length=50)
    parking = models.BooleanField(null=False)
    rent_price = models.PositiveIntegerField(default=0)
    deposit = models.PositiveIntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.neighborhood_name} --- {self.owner} --- rent : {self.rent_price} with deposit : {self.deposit} '

class sell_Contract(models.Model):
    buyer = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name="buyer")
    seller = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name="seller")
    expert = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name="sell_expert")
    status = models.CharField(max_length=20, null=False, blank=False, choices=[('first agreement', 'first agreement'),
                                                                              ('second agreement', 'second agreement')])
    property = models.ForeignKey(sell_Property, null=False, on_delete=models.CASCADE)
    tracking_code = models.CharField(max_length=20,default= " ",null=True)

    def __str__(self):
        return f' Buyer : {self.buyer} -- Seller : {self.seller} -- Expert : {self.expert} -- Status : {self.status}'


class rent_Contract(models.Model):
    renter = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name="renter")
    owner = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name="owner")
    expert = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE, related_name="rent_expert")
    status = models.CharField(max_length=20, null=False, blank=False, choices=[('first agreement', 'first agreement'),
                                                                              ('second agreement', 'second agreement')])
    property = models.ForeignKey(rent_Property, null=False, on_delete=models.CASCADE)
    tracking_code = models.CharField(max_length=20,default= " ",null=True)

    def __str__(self):
        return f' Renter : {self.renter} -- Owner : {self.owner} -- Expert : {self.expert} -- Status : {self.status}'



class customer (models.Model):
    MEMBER_SHIP = [
        ('B','Bronze'),
        ('S','Silver'),
        ('G','Gold')
    ]
    Name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)
    member_ship = models.CharField(max_length=1, choices=MEMBER_SHIP , default='B')

    def __str__(self):
        return self.Name

#
# class Address (models.Model):
#     city = models.CharField(max_length=225)
#     street = models.CharField(max_length=225)
#     customer = models.OneToOneField(customer,on_delete=models.CASCADE,primary_key=True)
#
#     property = models.ForeignKey(property,on_delete=models.CASCADE)









