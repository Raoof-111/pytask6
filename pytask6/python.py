
     
# İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək üçün metodlar.
# İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  super initdən  istifadə edəcəyik.   
# Bu classda bizim 2 metodumuz olacaq. Kredit vermək və kredit ödənişi. Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.
# Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).
     
class Hesab:
    def __init__(self, account_id, balans):
        self.account_id = account_id
        self.balans = balans

    def balans_artir(self, sum):
        self.balans += sum
        print("Balans artırıldı. Yeni balans:", self.balans)

    def pul_cixar(self, sum):
        if sum > self.balans:
            print("Balansınızda kifayət qədər vəsait yoxdur.")
        else:
            self.balans -= sum
            print("Balansdan", sum, "manat çıxarıldı. Yeni balans:", self.balans)

    def balans_qalıq(self):
        print("Hesab nömrəsi:", self.account_id)
        print("Cari balans:", self.balans)


class Kredit(Hesab):
    def __init__(self, account_id, balans, krsum):
        super().__init__(account_id, balans)
        self.krsum = krsum

    def kredit_ver(self):
        self.balans += self.krsum
        print("Kreditiniz hesabınıza əlavə olundu. Yeni balans:", self.balans)

    def kredit_odenisi(self):
        ayliq_odenis = self.krsum / 12
        if ayliq_odenis > self.balans:
            print("Kredit ödənişi üçün kifayət qədər vəsait yoxdur.")
        else:
            self.balans -= ayliq_odenis
            print("Kredit ödənişi uğurla həyata keçirildi. Yeni balans:", self.balans)



hesab1 = Hesab(1111, 111111)
hesab1.balans_qalıq()
hesab1.balans_artir(11)
hesab1.pul_cixar(1111)
hesab1.balans_qalıq()

print("\nKredit üçün:")
kredit1 = Kredit(111111, 111111111,111)
kredit1.balans_qalıq()
kredit1.kredit_ver()
kredit1.kredit_odenisi()
kredit1.balans_qalıq()



