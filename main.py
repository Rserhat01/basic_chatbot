from nltk.chat.util import Chat, reflections

ciftler = [
    ["Python nedir", ["Python, genel amaçlı bir programlama dilidir."]],
    ["Java nedir", ["Java, platform bağımsız çalışan bir programlama dilidir."]],
    ["HTML nedir", ["HTML, web sayfalarını oluşturmak için kullanılan bir işaretleme dilidir."]],
    ["CSS nedir", ["CSS, web sayfalarını tasarlamak için kullanılan bir stil dilidir."]],
    ["JavaScript nedir", ["JavaScript, web sayfalarına etkileşim eklemek için kullanılan bir programlama dilidir."]],
    ["SQL nedir", ["SQL, veri tabanlarını yönetmek için kullanılan bir sorgu dilidir."]],
    ["Veri tabanı nedir", ["Verilerin depolandığı ve yönetildiği bir yapıdır."]],
    ["OOP nedir", ["OOP (Nesne Tabanlı Programlama), programları nesneler ve sınıflar kullanarak yazma yöntemidir."]],
    ["API nedir", ["API, uygulamaların birbiriyle iletişim kurmasını sağlayan bir arabirimdir."]],
    ["REST API nedir", ["REST API, HTTP protokolü üzerinden çalışan bir API türüdür."]],
    ["Git nedir", ["Git, bir versiyon kontrol sistemidir."]],
    ["GitHub nedir", ["GitHub, Git kullanılarak oluşturulan projelerin barındırıldığı bir platformdur."]],
    ["Framework nedir", ["Framework, yazılım geliştirme için kullanılan bir yapı ve araçlar bütünüdür."]],
    ["Python'da fonksiyon nedir",
     ["Fonksiyon, tekrarlanan kodları daha düzenli hale getirmek için kullanılan bir yapıdır."]],
    ["Python'da döngü nedir", ["Döngü, belirli bir işlemi tekrar eden yapılardır (örneğin: for, while)."]],
    ["Python'da liste nedir", ["Liste, birden fazla öğeyi depolamak için kullanılan bir veri türüdür."]],
    ["Python'da dictionary nedir",
     ["Dictionary, anahtar-değer çiftlerini depolamak için kullanılan bir veri yapısıdır."]],
    ["Machine Learning nedir", ["Makine öğrenimi, verilerden öğrenerek tahmin yapabilen modeller oluşturmayı sağlar."]],
    ["Deep Learning nedir",
     ["Derin öğrenme, yapay sinir ağları kullanarak verilerden öğrenen bir makine öğrenimi yöntemidir."]],
    ["Scrum nedir", ["Scrum, çevik yazılım geliştirme yöntemlerinden biridir."]],
    ["Kanban nedir", ["Kanban, iş akışını görselleştirerek verimliliği artırmayı amaçlayan bir yöntemdir."]],
    ["Docker nedir", ["Docker, uygulamaları konteyner içinde çalıştırmayı sağlayan bir platformdur."]],
    ["Kubernetes nedir", ["Kubernetes, konteynerlerin yönetimi için kullanılan bir orkestrasyon aracıdır."]],
    ["DevOps nedir", ["DevOps, geliştirme ve operasyon ekipleri arasında iş birliğini artıran bir yaklaşımdır."]],
    ["Linux nedir", ["Linux, açık kaynaklı bir işletim sistemidir."]],
    ["Bash nedir", ["Bash, Linux ve Unix sistemlerde kullanılan bir kabuk programıdır."]],
    ["CI/CD nedir", ["CI/CD, sürekli entegrasyon ve sürekli dağıtım süreçlerini ifade eder."]],
    ["Unit test nedir", ["Unit test, bir yazılımın küçük birimlerini test etmek için kullanılan bir yöntemdir."]],
    ["Selenium nedir", ["Selenium, web uygulamalarını test etmek için kullanılan bir araçtır."]],
    ["React nedir", ["React, kullanıcı arayüzleri oluşturmak için kullanılan bir JavaScript kütüphanesidir."]],
    ["Node.js nedir", ["Node.js, JavaScript'in sunucu tarafında çalıştırılmasını sağlayan bir platformdur."]],
    ["Django nedir", ["Django, Python ile yazılmış bir web geliştirme framework'üdür."]],
    ["Flask nedir", ["Flask, Python ile yazılmış hafif bir web framework'üdür."]],
    ["Bootstrap nedir", ["Bootstrap, web sayfaları için tasarım şablonları sunan bir framework'tür."]],
    ["React Native nedir",
     ["React Native, mobil uygulamalar geliştirmek için kullanılan bir JavaScript framework'üdür."]],
    ["TypeScript nedir", ["TypeScript, JavaScript'in daha yapılandırılmış bir süper setidir."]],
    ["Pandas nedir", ["Pandas, veri analizi ve manipülasyonu için kullanılan bir Python kütüphanesidir."]],
    ["Numpy nedir", ["NumPy, bilimsel hesaplamalar için kullanılan bir Python kütüphanesidir."]],
    ["Matplotlib nedir", ["Matplotlib, veri görselleştirme için kullanılan bir Python kütüphanesidir."]],
    ["TensorFlow nedir", ["TensorFlow, makine öğrenimi modelleri geliştirmek için kullanılan bir kütüphanedir."]],
    ["PyTorch nedir", ["PyTorch, derin öğrenme için kullanılan bir Python kütüphanesidir."]],
    ["JSON nedir", ["JSON, veri alışverişi için kullanılan hafif bir veri formatıdır."]],
    ["XML nedir", ["XML, yapılandırılmış verileri taşımak için kullanılan bir işaretleme dilidir."]],
    ["JWT nedir", ["JWT, JSON tabanlı bir token yapısıdır ve kimlik doğrulama için kullanılır."]],
    ["ORM nedir", ["ORM, veri tabanı ile nesne yönelimli programlama arasındaki köprüdür."]],
    ["Yapay zeka nedir", ["Yapay zeka, makinelerin insanlar gibi düşünmesini sağlayan bir teknolojidir."]],
    ["API anahtarı nedir", ["API anahtarı, API erişimini kontrol eden bir kimlik doğrulama yöntemidir."]],
    ["Web scraping nedir", ["Web scraping, web sitelerinden veri çekme işlemidir."]]
]

yansimalar = {
    'merhaba':'merhaba, nasılsın?',
    'gittim':'gittin',
    'selamunaleyküm':'aleykümselam'
}

chat = Chat(ciftler, reflections)
chat.converse(quit='bitti')
#print(chat._substitute("merhaba"))
