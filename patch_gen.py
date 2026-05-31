import os

with open('generate_site.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hardcoded text with data-i18n tags

replacements = {
    # About
    '"text-muted" style="max-width: 600px; margin: 0 auto;">Pioneering wellness and pharmaceutical solutions for a healthier tomorrow.</p>': '"text-muted" style="max-width: 600px; margin: 0 auto;" data-i18n="about_subtitle">Pioneering wellness and pharmaceutical solutions for a healthier tomorrow.</p>',
    '<h2 class="mb-3">Our Vision & Mission</h2>': '<h2 class="mb-3" data-i18n="about_vision_title">Our Vision & Mission</h2>',
    '<p class="mb-3" style="line-height: 1.8;">NutraSakr is a premier healthcare and nutraceutical manufacturing corporation based in Egypt, proudly serving the MENA region, Africa, and global markets. We believe in the synergy between cutting-edge scientific innovation and natural wellness.</p>': '<p class="mb-3" style="line-height: 1.8;" data-i18n="about_vision_p1">NutraSakr is a premier healthcare and nutraceutical manufacturing corporation based in Egypt, proudly serving the MENA region, Africa, and global markets. We believe in the synergy between cutting-edge scientific innovation and natural wellness.</p>',
    '<p class="mb-3" style="line-height: 1.8;">Our mission is to empower individuals to live healthier lives by providing world-class, rigorously tested, and accessible nutritional supplements and pharmaceutical products.</p>': '<p class="mb-3" style="line-height: 1.8;" data-i18n="about_vision_p2">Our mission is to empower individuals to live healthier lives by providing world-class, rigorously tested, and accessible nutritional supplements and pharmaceutical products.</p>',
    '<h3 class="mb-2" style="color: var(--secondary-green);">15+</h3>': '<h3 class="mb-2" style="color: var(--secondary-green);" data-i18n="about_stat_1_val">15+</h3>',
    '<p class="text-muted">Global Markets Served</p>': '<p class="text-muted" data-i18n="about_stat_1_desc">Global Markets Served</p>',
    '<h3 class="mb-2" style="color: var(--secondary-green);">100%</h3>': '<h3 class="mb-2" style="color: var(--secondary-green);" data-i18n="about_stat_2_val">100%</h3>',
    '<p class="text-muted">Quality Guarantee</p>': '<p class="text-muted" data-i18n="about_stat_2_desc">Quality Guarantee</p>',
    '<h3 class="mb-2" style="color: var(--secondary-green);">Top Tier</h3>': '<h3 class="mb-2" style="color: var(--secondary-green);" data-i18n="about_stat_3_val">Top Tier</h3>',
    '<p class="text-muted">R&D Capabilities</p>': '<p class="text-muted" data-i18n="about_stat_3_desc">R&D Capabilities</p>',

    # Research
    '<p class="text-muted">Science-backed formulations engineered for efficacy.</p>': '<p class="text-muted" data-i18n="research_subtitle">Science-backed formulations engineered for efficacy.</p>',
    '<h3 class="mb-2">Product Development</h3>': '<h3 class="mb-2" data-i18n="research_card1_title">Product Development</h3>',
    '<p class="text-muted" style="line-height: 1.8;">Our dedicated R&D team continuously explores new bioactive compounds, optimizing bioavailability and stability to create next-generation supplements.</p>': '<p class="text-muted" style="line-height: 1.8;" data-i18n="research_card1_desc">Our dedicated R&D team continuously explores new bioactive compounds, optimizing bioavailability and stability to create next-generation supplements.</p>',
    '<h3 class="mb-2">Clinical Support</h3>': '<h3 class="mb-2" data-i18n="research_card2_title">Clinical Support</h3>',
    '<p class="text-muted" style="line-height: 1.8;">Every formulation is rooted in published scientific literature and clinical trials, ensuring that our products deliver measurable health benefits.</p>': '<p class="text-muted" style="line-height: 1.8;" data-i18n="research_card2_desc">Every formulation is rooted in published scientific literature and clinical trials, ensuring that our products deliver measurable health benefits.</p>',
    '<h3 class="mb-2">Regulatory Affairs</h3>': '<h3 class="mb-2" data-i18n="research_card3_title">Regulatory Affairs</h3>',
    '<p class="text-muted" style="line-height: 1.8;">We maintain strict compliance with local and international regulatory bodies (FDA, EFSA) to guarantee absolute safety.</p>': '<p class="text-muted" style="line-height: 1.8;" data-i18n="research_card3_desc">We maintain strict compliance with local and international regulatory bodies (FDA, EFSA) to guarantee absolute safety.</p>',
    '<h3 class="mb-2">Quality Assurance</h3>': '<h3 class="mb-2" data-i18n="research_card4_title">Quality Assurance</h3>',
    '<p class="text-muted" style="line-height: 1.8;">From raw material sourcing to final product testing, our in-house laboratories perform comprehensive microbiological and chemical analyses.</p>': '<p class="text-muted" style="line-height: 1.8;" data-i18n="research_card4_desc">From raw material sourcing to final product testing, our in-house laboratories perform comprehensive microbiological and chemical analyses.</p>',

    # Certs
    '<p class="text-muted">Uncompromising standards in every batch we produce.</p>': '<p class="text-muted" data-i18n="cert_subtitle">Uncompromising standards in every batch we produce.</p>',
    '<h2 style="color: var(--primary-blue); font-size: 2.5rem; margin-bottom: 10px;">GMP</h2>': '<h2 style="color: var(--primary-blue); font-size: 2.5rem; margin-bottom: 10px;" data-i18n="cert_gmp">GMP</h2>',
    '<h4 class="mb-2">Good Manufacturing Practice</h4>': '<h4 class="mb-2" data-i18n="cert_gmp_title">Good Manufacturing Practice</h4>',
    '<p class="text-muted">Certified compliance with strict international manufacturing and safety protocols.</p>': '<p class="text-muted" data-i18n="cert_gmp_desc">Certified compliance with strict international manufacturing and safety protocols.</p>',
    '<h2 style="color: var(--primary-blue); font-size: 2.5rem; margin-bottom: 10px;">ISO 9001</h2>': '<h2 style="color: var(--primary-blue); font-size: 2.5rem; margin-bottom: 10px;" data-i18n="cert_iso9001">ISO 9001</h2>',
    '<h4 class="mb-2">Quality Management</h4>': '<h4 class="mb-2" data-i18n="cert_iso9001_title">Quality Management</h4>',
    '<p class="text-muted">Ensuring consistent quality and continuous improvement across all operations.</p>': '<p class="text-muted" data-i18n="cert_iso9001_desc">Ensuring consistent quality and continuous improvement across all operations.</p>',
    '<h2 style="color: var(--primary-blue); font-size: 2.5rem; margin-bottom: 10px;">ISO 22000</h2>': '<h2 style="color: var(--primary-blue); font-size: 2.5rem; margin-bottom: 10px;" data-i18n="cert_iso22000">ISO 22000</h2>',
    '<h4 class="mb-2">Food Safety Management</h4>': '<h4 class="mb-2" data-i18n="cert_iso22000_title">Food Safety Management</h4>',
    '<p class="text-muted">Highest level of food safety systems for nutritional and dietary supplements.</p>': '<p class="text-muted" data-i18n="cert_iso22000_desc">Highest level of food safety systems for nutritional and dietary supplements.</p>',

    # Private Label
    '<p class="text-muted">Bring your brand to life with our end-to-end manufacturing expertise.</p>': '<p class="text-muted" data-i18n="pl_subtitle">Bring your brand to life with our end-to-end manufacturing expertise.</p>',
    '<h2 class="mb-3">Turnkey Manufacturing</h2>': '<h2 class="mb-3" data-i18n="pl_title">Turnkey Manufacturing</h2>',
    '<p class="mb-3" style="line-height: 1.8;">NutraSakr offers premium B2B contract manufacturing. From custom formula design to final retail packaging, we handle the entire process.</p>': '<p class="mb-3" style="line-height: 1.8;" data-i18n="pl_desc">NutraSakr offers premium B2B contract manufacturing. From custom formula design to final retail packaging, we handle the entire process.</p>',
    '<li>💊 <strong>Formula Design:</strong> Custom blends tailored to your market.</li>': '<li data-i18n="pl_li1">💊 <strong>Formula Design:</strong> Custom blends tailored to your market.</li>',
    '<li>🏭 <strong>Production:</strong> High-capacity tableting, encapsulation, and powders.</li>': '<li data-i18n="pl_li2">🏭 <strong>Production:</strong> High-capacity tableting, encapsulation, and powders.</li>',
    '<li>🏷️ <strong>Packaging & Design:</strong> Blisters, bottles, sachets, and label design.</li>': '<li data-i18n="pl_li3">🏷️ <strong>Packaging & Design:</strong> Blisters, bottles, sachets, and label design.</li>',
    '<li>📜 <strong>Regulatory Support:</strong> Dossier preparation and export registration.</li>': '<li data-i18n="pl_li4">📜 <strong>Regulatory Support:</strong> Dossier preparation and export registration.</li>',
    '<a href="contact.html" class="btn btn-primary">Request a Quote</a>': '<a href="contact.html" class="btn btn-primary" data-i18n="pl_btn">Request a Quote</a>',

    # Export
    '<p class="text-muted">Delivering premium Egyptian healthcare solutions to the world.</p>': '<p class="text-muted" data-i18n="export_subtitle">Delivering premium Egyptian healthcare solutions to the world.</p>',
    '<p style="max-width: 700px; margin: 0 auto 40px; font-size: 1.1rem; line-height: 1.8;">NutraSakr is rapidly expanding its global footprint. We currently distribute our high-quality nutraceuticals and medical supplements across the GCC, North Africa, and select international markets.</p>': '<p style="max-width: 700px; margin: 0 auto 40px; font-size: 1.1rem; line-height: 1.8;" data-i18n="export_desc">NutraSakr is rapidly expanding its global footprint. We currently distribute our high-quality nutraceuticals and medical supplements across the GCC, North Africa, and select international markets.</p>',
    '<h3 class="mb-2">Africa & MENA</h3>': '<h3 class="mb-2" data-i18n="export_card1_title">Africa & MENA</h3>',
    '<p class="text-muted">Strong logistics network across regional markets.</p>': '<p class="text-muted" data-i18n="export_card1_desc">Strong logistics network across regional markets.</p>',
    '<h3 class="mb-2">GCC</h3>': '<h3 class="mb-2" data-i18n="export_card2_title">GCC</h3>',
    '<p class="text-muted">Compliant with Saudi FDA and regional health ministries.</p>': '<p class="text-muted" data-i18n="export_card2_desc">Compliant with Saudi FDA and regional health ministries.</p>',
    '<h3 class="mb-2">International</h3>': '<h3 class="mb-2" data-i18n="export_card3_title">International</h3>',
    '<p class="text-muted">Expanding our footprint into Europe and Asia.</p>': '<p class="text-muted" data-i18n="export_card3_desc">Expanding our footprint into Europe and Asia.</p>',
    '<a href="distributors.html" class="btn btn-secondary">Join Our Distribution Network</a>': '<a href="distributors.html" class="btn btn-secondary" data-i18n="export_btn">Join Our Distribution Network</a>',

    # Distributors
    '<h1 class="mb-2">Become a Distributor</h1>': '<h1 class="mb-2" data-i18n="dist_title">Become a Distributor</h1>',
    '<p class="text-muted">Partner with NutraSakr for exclusive market opportunities.</p>': '<p class="text-muted" data-i18n="dist_subtitle">Partner with NutraSakr for exclusive market opportunities.</p>',
    '<h2 class="mb-3">Why Partner With Us?</h2>': '<h2 class="mb-3" data-i18n="dist_why">Why Partner With Us?</h2>',
    '<li>✅ Highly competitive wholesale pricing</li>': '<li data-i18n="dist_li1">✅ Highly competitive wholesale pricing</li>',
    '<li>✅ Premium, fast-moving product portfolio</li>': '<li data-i18n="dist_li2">✅ Premium, fast-moving product portfolio</li>',
    '<li>✅ Marketing and scientific training support</li>': '<li data-i18n="dist_li3">✅ Marketing and scientific training support</li>',
    '<li>✅ Dedicated account management</li>': '<li data-i18n="dist_li4">✅ Dedicated account management</li>',
    '<li>✅ Flexible minimum order quantities</li>': '<li data-i18n="dist_li5">✅ Flexible minimum order quantities</li>',

    # News
    '<h1 class="mb-2">News & Insights</h1>': '<h1 class="mb-2" data-i18n="nav_news">News & Insights</h1>',
    '<p class="text-muted">Latest updates from NutraSakr and the healthcare industry.</p>': '<p class="text-muted" data-i18n="news_subtitle">Latest updates from NutraSakr and the healthcare industry.</p>',
    '<p class="text-muted" style="margin-bottom: 40px;">Check back soon for upcoming press releases, product launches, and scientific articles.</p>': '<p class="text-muted" style="margin-bottom: 40px;" data-i18n="news_desc">Check back soon for upcoming press releases, product launches, and scientific articles.</p>',

    # Careers
    '<h1 class="mb-2">Careers</h1>': '<h1 class="mb-2" data-i18n="nav_careers">Careers</h1>',
    '<p class="text-muted">Join the team shaping the future of healthcare.</p>': '<p class="text-muted" data-i18n="careers_subtitle">Join the team shaping the future of healthcare.</p>',
    '<p class="text-muted">We are always looking for talented professionals in R&D, Quality Control, Sales, and Production. Please send your CV to <a href="mailto:hr@nutrasakr.com">hr@nutrasakr.com</a>.</p>': '<p class="text-muted" data-i18n="careers_desc">We are always looking for talented professionals in R&D, Quality Control, Sales, and Production. Please send your CV to hr@nutrasakr.com.</p>',

    # Request Info
    '<h1 class="mb-2">Request Information</h1>': '<h1 class="mb-2" data-i18n="btn_request_info">Request Information</h1>',
    '<p class="text-muted">Our team is ready to provide detailed dossiers and catalogs.</p>': '<p class="text-muted" data-i18n="req_subtitle">Our team is ready to provide detailed dossiers and catalogs.</p>',
    '<a href="contact.html" class="btn btn-primary">Go to Contact Form</a>': '<a href="contact.html" class="btn btn-primary" data-i18n="req_btn">Go to Contact Form</a>',

    # Privacy
    '<h1 class="mb-2">Privacy Policy</h1>': '<h1 class="mb-2" data-i18n="privacy_title">Privacy Policy</h1>',
    '<p class="mb-3">NutraSakr respects your privacy and is committed to protecting your personal data. This policy outlines how we collect, process, and safeguard your information when you visit our website.</p>': '<p class="mb-3" data-i18n="privacy_p1">NutraSakr respects your privacy and is committed to protecting your personal data. This policy outlines how we collect, process, and safeguard your information when you visit our website.</p>',
    '<h3 class="mb-2">Data Collection</h3>': '<h3 class="mb-2" data-i18n="privacy_h1">Data Collection</h3>',
    '<p class="mb-3">We only collect data that you voluntarily provide via our contact forms (Name, Email, Phone, Company) for the purpose of responding to your inquiries.</p>': '<p class="mb-3" data-i18n="privacy_p2">We only collect data that you voluntarily provide via our contact forms (Name, Email, Phone, Company) for the purpose of responding to your inquiries.</p>',
    '<h3 class="mb-2">Data Usage</h3>': '<h3 class="mb-2" data-i18n="privacy_h2">Data Usage</h3>',
    '<p class="mb-3">Your information is never sold to third parties. It is used strictly for internal business communication, order processing, and customer support.</p>': '<p class="mb-3" data-i18n="privacy_p3">Your information is never sold to third parties. It is used strictly for internal business communication, order processing, and customer support.</p>',

    # Terms
    '<h1 class="mb-2">Terms & Conditions</h1>': '<h1 class="mb-2" data-i18n="terms_title">Terms & Conditions</h1>',
    '<p class="mb-3">Welcome to the NutraSakr corporate website. By accessing and using this site, you agree to comply with our terms of service.</p>': '<p class="mb-3" data-i18n="terms_p1">Welcome to the NutraSakr corporate website. By accessing and using this site, you agree to comply with our terms of service.</p>',
    '<h3 class="mb-2">Intellectual Property</h3>': '<h3 class="mb-2" data-i18n="terms_h1">Intellectual Property</h3>',
    '<p class="mb-3">All content, logos, text, imagery, and product designs on this website are the intellectual property of NutraSakr and may not be copied, reproduced, or distributed without written consent.</p>': '<p class="mb-3" data-i18n="terms_p2">All content, logos, text, imagery, and product designs on this website are the intellectual property of NutraSakr and may not be copied, reproduced, or distributed without written consent.</p>',
    '<h3 class="mb-2">Medical Disclaimer</h3>': '<h3 class="mb-2" data-i18n="terms_h2">Medical Disclaimer</h3>',
    '<p class="mb-3">The information provided on this website is for corporate and informational purposes only and is not intended as medical advice. Consumers should always consult a healthcare professional before starting any supplement regimen.</p>': '<p class="mb-3" data-i18n="terms_p3">The information provided on this website is for corporate and informational purposes only and is not intended as medical advice. Consumers should always consult a healthcare professional before starting any supplement regimen.</p>'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('generate_site.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied to generate_site.py successfully.")
