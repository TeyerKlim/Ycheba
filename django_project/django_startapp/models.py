from django.db import models

class Motorcycle_dealership(models.Model):
    Motorcycle_dealership_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'Motorcycle_dealership'
        verbose_name = 'Мотосалон'
        verbose_name_plural = 'Мотосалоны'
    
    def __str__(self):
        return self.Title

class Dealer(models.Model):
    Dealer_id = models.AutoField(primary_key=True)
    Surname = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Middle_name = models.CharField(max_length=255)
    Phone_number = models.IntegerField()
    
    class Meta:
        db_table = 'Dealer'
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'
    
    def __str__(self):
        return f"{self.Surname} {self.Name} {self.Middle_name}"

class Client(models.Model):
    Client_id = models.AutoField(primary_key=True)
    Surname = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Middle_name = models.CharField(max_length=255)
    Phone_number = models.IntegerField()
    Driving_license = models.BooleanField()
    
    class Meta:
        db_table = 'Client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    def __str__(self):
        return f"{self.Surname} {self.Name} {self.Middle_name}"

class Motorcycle_transport(models.Model):
    Motorcycle_transport_id = models.AutoField(primary_key=True)
    Motorcycle_dealership = models.ForeignKey(
        Motorcycle_dealership, 
        on_delete=models.CASCADE,
        db_column='Motorcycle_dealership_id'
    )
    Type = models.CharField(max_length=255)
    Price = models.IntegerField()
    Year_of_release = models.IntegerField()
    Brand = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'Motorcycle_transport'
        verbose_name = 'Мототранспорт'
        verbose_name_plural = 'Мототранспорт'
    
    def __str__(self):
        return f"{self.Brand} {self.Model} ({self.Year_of_release})"

class Accessories(models.Model):
    Accessories_id = models.AutoField(primary_key=True)
    motorcycle_dealership = models.ForeignKey(
        Motorcycle_dealership, 
        on_delete=models.CASCADE,
        db_column='Motorcycle_dealership_id'
    )
    Title = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Brand = models.CharField(max_length=255)
    Price = models.IntegerField()
    
    class Meta:
        db_table = 'Accessories'
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
    
    def __str__(self):
        return f"{self.Brand} {self.Title}"

class Services(models.Model):
    Services_id = models.AutoField(primary_key=True)
    Motorcycle_dealership = models.ForeignKey(
        Motorcycle_dealership, 
        on_delete=models.CASCADE,
        db_column='Motorcycle_dealership_id'
    )
    Price = models.IntegerField()
    Repair = models.CharField(max_length=255, blank=True, null=True)
    Test_drive = models.CharField(max_length=255, blank=True, null=True)
    Technical_maintenance = models.CharField(max_length=255, blank=True, null=True)
    Sale_Motorcycle_transport = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'Services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    
    def __str__(self):
        return f"Service {self.Services_id}"

class Deal(models.Model):
    Deal_id = models.AutoField(primary_key=True)
    Dealer = models.ForeignKey(
        Dealer, 
        on_delete=models.CASCADE,
        db_column='Dealer_id'
    )
    Client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE,
        db_column='Client_id'
    )
    
    class Meta:
        db_table = 'Deal'
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
    
    def __str__(self):
        return f"Deal {self.Deal_id}"

class DealMotorcycletransport(models.Model):
    Deal_Motorcycle_transport_id = models.AutoField(primary_key=True)
    Motorcycle_transport = models.ForeignKey(
        Motorcycle_transport, 
        on_delete=models.CASCADE,
        db_column='Motorcycle_transport_id'
    )
    Deal = models.ForeignKey(
        Deal, 
        on_delete=models.CASCADE,
        db_column='Deal_id'
    )
    
    class Meta:
        db_table = 'Deal_Motorcycle_transport'
        verbose_name = 'Сделка-Мототранспорт'
        verbose_name_plural = 'Сделка-Мототранспорт'

class DealServices(models.Model):
    Deal_Services_id = models.AutoField(primary_key=True)
    Services = models.ForeignKey(
        Services, 
        on_delete=models.CASCADE,
        db_column='Services_id'
    )
    Deal = models.ForeignKey(
        Deal, 
        on_delete=models.CASCADE,
        db_column='Deal_id'
    )
    
    class Meta:
        db_table = 'Deal_Services'
        verbose_name = 'Сделка-Услуги'
        verbose_name_plural = 'Сделка-Услуги'

class DealAccessories(models.Model):
    Deal_Accessories_id = models.AutoField(primary_key=True)
    Accessories = models.ForeignKey(
        Accessories, 
        on_delete=models.CASCADE,
        db_column='Accessories_id'
    )
    Deal = models.ForeignKey(
        Deal, 
        on_delete=models.CASCADE,
        db_column='Deal_id'
    )
    
    class Meta:
        db_table = 'Deal_Accessories'
        verbose_name = 'Сделка-Аксессуары'
        verbose_name_plural = 'Сделка-Аксессуары'