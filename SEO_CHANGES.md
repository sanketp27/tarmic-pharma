# Proposed Product Page Content Layout & SEO Changes

## 1. Proposed Product Page Content Template

This proposed layout is designed for product pages to expand beyond basic composition/pricing while adhering strictly to Indian regulatory standards (Drugs and Cosmetics Act & Rules). 

**Do not invent indications, claims, or storage conditions.** A human medical/regulatory expert must populate the `[[TODO]]` placeholders directly from approved carton artwork, package inserts, and Form 20B/21B licences.

```html
<!-- Proposed Product Information Layout -->
<section class="product-details-container">
  <div class="wrap pd">
    <!-- Image Box -->
    <div class="pdimg">
      <img src="images/[[TODO: image-file-slug]].jpg" alt="[[TODO: BRAND NAME]] pack: [[TODO: full approved composition]]">
    </div>

    <!-- Product Summary & Specifications -->
    <div class="pdinfo">
      <p class="cat">[[TODO: Therapy Area / Category]]</p>
      <h1>[[TODO: BRAND NAME]]</h1>
      <p class="sub">[[TODO: Generic Name(s) and Dosage Form, e.g., Bilastine &amp; Montelukast Tablets]]</p>

      <!-- Section: Product Details -->
      <section class="pd-section" id="product-details">
        <h2>Product Details</h2>
        <dl>
          <dt>Composition</dt>
          <dd>[[TODO: Active pharmaceutical ingredients and strengths from approved label, e.g., Each film coated tablet contains: Glimepiride IP 1 mg, Metformin Hydrochloride IP 500 mg (in sustained release form)]]</dd>
          
          <dt>Dosage Form</dt>
          <dd>[[TODO: Tablets / Capsules / Dispersible Tablets / Modified Release]]</dd>

          <dt>Packing</dt>
          <dd>[[TODO: Strip / Blister / Alu-Alu packing, e.g., 10x10 Tablets]]</dd>

          <dt>MRP</dt>
          <dd class="price">[[TODO: Printed Maximum Retail Price per strip, inclusive of all taxes]]</dd>

          <dt>Marketed by</dt>
          <dd>Tarmic Pharma Pvt. Ltd.</dd>

          <dt>Manufactured by</dt>
          <dd>[[TODO: Licensed manufacturer name, manufacturing facility address, and Drug Manufacturing Licence Number]]</dd>
        </dl>
      </section>

      <!-- Section: Indication -->
      <section class="pd-section" id="indication">
        <h2>Indication</h2>
        <div class="content-block">
          <p>[[TODO: Approved therapeutic indication(s) as per CDSCO / DCGI approved product package insert. Do not add off-label or unverified claims.]]</p>
          <p><strong>Dosage:</strong> [[TODO: As directed by the Registered Medical Practitioner.]]</p>
        </div>
      </section>

      <!-- Section: Storage -->
      <section class="pd-section" id="storage">
        <h2>Storage Conditions</h2>
        <div class="content-block">
          <p>[[TODO: Storage instructions as printed on approved carton artwork, e.g., Store protected from light and moisture at a temperature not exceeding 25°C / 30°C. Keep medicine out of reach of children.]]</p>
        </div>
      </section>

      <!-- Section: Prescription Statement -->
      <section class="pd-section prescription-box" id="prescription-statement">
        <h2>Prescription Statement</h2>
        <div class="warning-callout">
          <p class="rx-warning"><strong>[[TODO: Schedule Warning]]:</strong> [[TODO: Statutory warning text, e.g., SCHEDULE H PRESCRIPTION DRUG - CAUTION: To be sold by retail on the prescription of a Registered Medical Practitioner only. / SCHEDULE H1 PRESCRIPTION DRUG - CAUTION: It is dangerous to take this preparation except in accordance with the medical advice.]]</p>
          <p class="note">Prescription medicines should be used only on the advice of a registered medical practitioner. MRP is per strip as printed in the catalogue and may change; please confirm with us before ordering.</p>
        </div>
      </section>

      <!-- Call to Action -->
      <div class="cta">
        <a class="btn" href="mailto:operations@tarmic.in?subject=[[TODO: URL-encoded mailto subject]]">Enquire about [[TODO: BRAND NAME]]</a>
        <a class="btn line" href="[[TODO: category-page-url.html]]">More in this category</a>
      </div>
    </div>
  </div>
</section>
```

---

## 2. Guide to Activating Draft Pages (about.html & contact.html)

Once legal and MCA details have been confirmed by management:
1. **Remove `noindex` tag**: In both `about.html` and `contact.html`, remove or change `<meta name="robots" content="noindex">` to `<meta name="robots" content="index,follow">`.
2. **Add navigation and footer links**:
   - In `<header>` nav across all HTML templates: update links from `#about` / `#contact` anchors to `about.html` and `contact.html`.
   - In `<footer>` under "Explore": add links to `about.html` and `contact.html`.
3. **Include in Sitemap**:
   - In `generate_sitemap.py`, remove `"about"` and `"contact"` from `EXCLUDED_STEMS`.
   - Re-run `python3 generate_sitemap.py` to regenerate `sitemap.xml`.
