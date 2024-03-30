import discord
import asyncio
import random

TOKEN = 'BOT TOKEN BURAYA'

ENVIRONMENT_MESSAGES = [
    "Doğayı korumak, geleceğimizi korumaktır.",
    "Her damla suyun kıymetini bil.",
    "Bir ağaç dik, bir nefes yeşert.",
    "Doğaya saygı, yaşamın sürdürülebilirliğidir.",
    "Atıklarınızı geri dönüşüme kazandırın.",
    "Biriktirdiğiniz çöpleri doğru bir şekilde atın.",
    "Plastik kullanımını minimuma indirin.",
    "Sürdürülebilir enerji kaynaklarına destek olun.",
    "Yerel ürünleri tercih edin, taşıma maliyetlerini azaltın.",
    "Doğal kaynakları israf etmeyin.",
    "Denizlere plastik atıklarınızı bırakmayın.",
    "Çevre dostu temizlik ürünleri kullanın.",
    "Enerji tasarrufu sağlayan cihazlar tercih edin.",
    "Bisiklet veya toplu taşıma araçlarını kullanarak karbon ayak izinizi azaltın.",
    "Doğal yaşam alanlarını korumak için yerel doğa koruma projelerine destek olun.",
    "Bahçenizde böcek ilaçları yerine doğal yöntemler kullanın.",
    "Plastik poşet kullanmamaya özen gösterin.",
    "Kıyı temizlik etkinliklerine katılın.",
    "Geri dönüştürülmüş kağıt ürünleri tercih edin.",
    "Atık suyunuzu geri dönüşüme kazandırın.",
    "Tek kullanımlık plastik ürünleri tercih etmeyin.",
    "Doğal yaşam alanlarına zarar vermemek için dikkatli olun.",
    "Bahçenizde organik tarım uygulamaları yapın.",
    "Geri dönüştürülebilir ambalajları tercih edin.",
    "Orman yangınlarını önlemek için dikkatli olun.",
    "Çevreyi kirleten faaliyetlere karşı çıkın.",
    "Sık sık doğada temizlik yapın.",
    "Doğal su kaynaklarını kirletmeyin.",
    "Atıklarınızı ayrıştırın.",
    "Fosil yakıtlara alternatif enerji kaynaklarına yatırım yapın.",
    "Doğal yaşam alanlarını korumak için bilinçli olun.",
    "Çevre dostu bir yaşam tarzı benimseyin.",
    "Kirli enerji kaynaklarına alternatif arayışları destekleyin.",
    "Çevre eğitimi programlarına katılın.",
    "Atık miktarını azaltmak için yeniden kullanım yapın.",
    "Tarımda organik yöntemleri destekleyin.",
    "Yerel su kaynaklarını koruyun.",
    "Kullanılmış eşyalarınızı geri dönüşüme kazandırın.",
    "Doğal yaşam alanlarını koruyarak biyoçeşitliliği destekleyin.",
    "Çevre bilinci oluşturmak için toplum etkinliklerine katılın.",
    "Endüstriyel atıkları minimuma indirmek için çalışın.",
    "Doğa yürüyüşleri yaparak çevreyi keşfedin.",
    "Çevre sorunlarına karşı duyarlılık geliştirin.",
    "Doğal yaşam alanlarında çevre bilinci oluşturun.",
    "Kullanılmış pilleri geri dönüşüme kazandırın.",
    "Kirli su kaynaklarını temizlemek için gönüllü olun.",
    "Atık azaltma kampanyalarına katılın.",
    "Ekolojik ayak izinizi hesaplayın ve azaltma stratejileri geliştirin.",
    "Çevre dostu ürünleri destekleyin.",
    "Yerel su kirliliği sorunlarına karşı mücadele edin.",
    "Atık elektronik eşyalarınızı geri dönüşüme kazandırın.",
    "Okullarda çevre eğitimi programlarını teşvik edin.",
    "Ormanları korumak için fidan dikim etkinliklerine katılın.",
    "Gıda israfını minimuma indirin.",
    "Kıyı bölgelerini korumak için sahil temizliği etkinliklerine katılın.",
    "Düşük karbonlu taşıma yöntemlerini destekleyin.",
    "Sıfır atık hedefiyle hareket edin.",
    "Su tasarrufu sağlayan yöntemleri benimseyin.",
    "Çevre dostu inşaat malzemelerini tercih edin.",
    "Doğal yaşam alanlarını korumak için bilinçli tüketici olun.",
    "Çevre sorunları hakkında bilinçlendirme kampanyalarına destek olun.",
    "Atık su arıtma tesislerini destekleyin.",
    "Atık ayrıştırma tesislerine yatırım yapın.",
    "Gıda ve tarım sektöründe sürdürülebilir uygulamaları destekleyin.",
    "Toplumsal çevre sorunlarına duyarlılık geliştirin.",
    "Denizlerdeki plastik kirliliğiyle mücadele edin.",
    "Orman yangınlarını önlemek için bilinçli olun.",
    "Çevre dostu taşımacılık sistemlerini destekleyin.",
    "Endüstriyel atıkların geri dönüşümünü teşvik edin.",
    "Tarımda su verimliliğini artırmak için çalışın.",
    "Kirliliğe neden olan faaliyetleri raporlayın.",
    "Çevre koruma yasalarını destekleyin.",
    "Su kirliliği sorunlarını çözmek için hepimiz sorumluluk almalıyız.",
    "Çevre felaketlerini önlemek için eyleme geçin.",
    "Doğayı korumak, gelecek nesillere temiz bir dünya bırakmaktır.",
    "Sürdürülebilir turizmi destekleyin, doğal yaşam alanlarını koruyun.",
    "Atıklarınızı geri dönüştürerek kaynakları koruyun.",
    "Çevre bilinci oluşturmak için eğitim programları düzenleyin.",
    "Su tasarrufu yaparak su kaynaklarını koruyun.",
    "Çevre dostu alışveriş alışkanlıkları edinin.",
    "Sera gazı emisyonlarını azaltmak için karbon ayak izinizi hesaplayın.",
    "Doğa koruma alanlarına katkıda bulunarak habitatları koruyun.",
    "Evcil hayvanlarınızın atıklarını doğru bir şekilde bertaraf edin.",
    "Kamusal alanlarda temizlik etkinliklerine katılın.",
    "Enerji verimli ev aletleri kullanarak enerji tasarrufu sağlayın.",
    "Kuraklık dönemlerinde su kullanımını azaltın.",
    "Hava kirliliğiyle mücadele etmek için fosil yakıtlara alternatif enerji kaynaklarını destekleyin.",
    "Sürdürülebilir tarım uygulamalarını destekleyin.",
    "Çevre sorunları hakkında farkındalık yaratmak için sosyal medyayı kullanın.",
    "Toprak erozyonunu önlemek için erozyon kontrol önlemleri alın.",
    "Sürdürülebilir yaşam tarzı benimseyerek doğal kaynakları koruyun.",
    "Denizlerdeki plastik atıkları temizlemek için deniz temizliği etkinliklerine katılın.",
    "Çevre sorunlarına karşı kamuoyu baskısını artırın.",
    "Kuruluşların çevresel etkilerini azaltmaları için teşvik edici politikalar destekleyin.",
    "Doğal afetlerin etkilerini azaltmak için önlem alın.",
    "Çevre dostu bir ofis ortamı oluşturun.",
    "Sürdürülebilir moda markalarını destekleyin.",
    "Atık elektrikli eşyalarınızı doğru bir şekilde bertaraf edin.",
    "Nehir ve göllerin temiz kalması için çevre koruma projelerine katılın.",
    "Habitat kayıplarını önlemek için doğal yaşam alanlarını koruyun.",
    "Gelecek nesillere temiz bir dünya bırakmak için bugün harekete geçin.",
    "Doğa dostu turizm destinasyonlarını tercih edin.",
    "Yiyecek ve içecek tüketiminde israfı önleyin.",
    "Bisiklet kullanarak çevreyi koruyun ve sağlıklı bir yaşam tarzı benimseyin.",
    "Atık miktarını azaltmak için ambalajlı ürünler yerine dökme ürünleri tercih edin.",
    "Yeşil enerji üretimi projelerini destekleyin.",
    "Çevre sorunlarına karşı hükümeti ve yerel yönetimleri sorumlu tutun.",
    "Gönüllü olarak çevre koruma projelerine katılın.",
    "Eğitim kurumlarına çevre eğitimi programları eklenmesini destekleyin.",
    "Orman yangınlarını önlemek için doğru yangın güvenlik önlemlerini alın.",
    "Tarımda organik yöntemleri destekleyin ve kimyasal kullanımını azaltın.",
    "Doğa rezervleri ve milli parklara destek verin.",
    "Çevre dostu teknolojilere yatırım yapın.",
    "Sürdürülebilir kentleşme projelerini destekleyin.",
    "Plajlarda çöplerinizi doğru bir şekilde atın.",
    "Eğitim kurumlarında geri dönüşüm programlarını destekleyin.",
    "Kirliliğe neden olan faaliyetleri raporlayın ve önlem alın.",
    "Su kirliliği sorunlarını çözmek için hepimiz sorumluluk almalıyız.",
    "Çevre felaketlerini önlemek için eyleme geçin.",
    "Doğayı korumak, gelecek nesillere temiz bir dünya bırakmaktır.",
    "Sürdürülebilir turizmi destekleyin, doğal yaşam alanlarını koruyun.",
    "Atıklarınızı geri dönüştürerek kaynakları koruyun.",
    "Çevre bilinci oluşturmak için eğitim programları düzenleyin.",
    "Su tasarrufu yaparak su kaynaklarını koruyun.",
    "Çevre dostu alışveriş alışkanlıkları edinin.",
    "Sera gazı emisyonlarını azaltmak için karbon ayak izinizi hesaplayın.",
    "Doğa koruma alanlarına katkıda bulunarak habitatları koruyun.",
    "Evcil hayvanlarınızın atıklarını doğru bir şekilde bertaraf edin.",
    "Kamusal alanlarda temizlik etkinliklerine katılın.",
    "Enerji verimli ev aletleri kullanarak enerji tasarrufu sağlayın.",
    "Kuraklık dönemlerinde su kullanımını azaltın.",
    "Hava kirliliğiyle mücadele etmek için fosil yakıtlara alternatif enerji kaynaklarını destekleyin.",
    "Sürdürülebilir tarım uygulamalarını destekleyin.",
    "Sıfır atık hedefiyle hareket edin.",
    "Doğa yürüyüşleri yaparak çevreyi keşfedin.",
    "Çevre sorunlarına karşı duyarlılık geliştirin.",
    "Doğal yaşam alanlarında çevre bilinci oluşturun.",
    "Kullanılmış pilleri geri dönüşüme kazandırın.",
    "Kirli su kaynaklarını temizlemek için gönüllü olun.",
    "Atık azaltma kampanyalarına katılın.",
    "Ekolojik ayak izinizi hesaplayın ve azaltma stratejileri geliştirin.",
    "Çevre dostu ürünleri destekleyin.",
    "Yerel su kirliliği sorunlarına karşı mücadele edin.",
    "Atık elektronik eşyalarınızı geri dönüşüme kazandırın.",
    "Okullarda çevre eğitimi programlarını teşvik edin.",
    "Ormanları korumak için fidan dikim etkinliklerine katılın.",
    "Gıda israfını minimuma indirin.",
    "Kıyı bölgelerini korumak için sahil temizliği etkinliklerine katılın.",
    "Düşük karbonlu taşıma yöntemlerini destekleyin.",
    "Sıfır atık hedefiyle hareket edin.",
    "Su tasarrufu sağlayan yöntemleri benimseyin.",
    "Çevre dostu inşaat malzemelerini tercih edin.",
    "Doğal yaşam alanlarını korumak için bilinçli tüketici olun.",
    "Çevre sorunları hakkında bilinçlendirme kampanyalarına destek olun.",
    "Atık su arıtma tesislerini destekleyin.",
    "Atık ayrıştırma tesislerine yatırım yapın.",
    "Gıda ve tarım sektöründe sürdürülebilir uygulamaları destekleyin.",
    "Toplumsal çevre sorunlarına duyarlılık geliştirin.",
    "Denizlerdeki plastik kirliliğiyle mücadele edin.",
    "Orman yangınlarını önlemek için bilinçli olun.",
    "Çevre dostu taşımacılık sistemlerini destekleyin.",
    "Endüstriyel atıkların geri dönüşümünü teşvik edin.",
    "Tarımda su verimliliğini artırmak için çalışın.",
    "Kirliliğe neden olan faaliyetleri raporlayın.",
    "Çevre koruma yasalarını destekleyin.",
]

CHANNEL_NAME = 'duyurular'

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)

# Last 10 messages sent
last_messages = []

# Function to fetch a random image related to the message
async def fetch_image(query):
    # Implement fetching image logic using a reliable service/API
    # Example: Use Unsplash API for fetching images
    return None

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    duyurular_channel = discord.utils.get(client.get_all_channels(), name=CHANNEL_NAME)
    if duyurular_channel is None:
        print(f"Could not find a channel named '{CHANNEL_NAME}'.")
        return

    # Loop to send a message every day
    while True:
        # Fetch a random message
        message = random.choice(ENVIRONMENT_MESSAGES)

        # Fetch a related image
        query = message.split(',')[0]  # Take the first word of the message as the search query
        image_url = await fetch_image(query)

        # Check if the message is not among the last 10 messages sent
        if message not in last_messages and image_url:
            # Send the message
            try:
                await duyurular_channel.send(message)
                await duyurular_channel.send(image_url)
                last_messages.append(message)
            except discord.errors.Forbidden:
                print("Bot doesn't have permission to send messages to the channel.")
                break
            except discord.errors.HTTPException:
                print("An error occurred while sending the message.")
                break

            if len(last_messages) > 25:
                last_messages.pop(0)

        await asyncio.sleep(5)  # Send message every 24 hours (86400 seconds)

client.run(TOKEN)
