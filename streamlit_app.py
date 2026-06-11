<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexara Finance | Servicios Financieros Premium para Pymes</title>
    <style>
        :root {
            --primary-color: #0f2027; /* Azul marino profundo */
            --secondary-color: #203a43;
            --accent-color: #2c5364;
            --highlight-color: #00adb5; /* Turquesa para llamadas a la acción */
            --text-dark: #333333;
            --text-light: #ffffff;
            --bg-light: #f4f7f6;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-light);
            color: var(--text-dark);
            line-height: 1.6;
        }

        /* Header / Navbar */
        header {
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            color: var(--text-light);
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .logo h1 {
            font-size: 24px;
            font-weight: 700;
            letter-spacing: 1px;
        }

        .logo span {
            color: var(--highlight-color);
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(15, 32, 39, 0.85), rgba(44, 83, 100, 0.85)), url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1950&q=80') no-repeat center center/cover;
            color: var(--text-light);
            padding: 100px 20px;
            text-align: center;
        }

        .hero h2 {
            font-size: 42px;
            margin-bottom: 20px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero p {
            font-size: 18px;
            margin-bottom: 30px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            opacity: 0.9;
        }

        .btn-cta {
            background-color: var(--highlight-color);
            color: var(--text-light);
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            transition: all 0.3s ease;
            display: inline-block;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 173, 181, 0.4);
        }

        .btn-cta:hover {
            background-color: #008c95;
            transform: translateY(-2px);
        }

        /* Philosophy & Pillars */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        .section-title {
            text-align: center;
            font-size: 32px;
            color: var(--primary-color);
            margin-bottom: 40px;
            position: relative;
        }

        .section-title::after {
            content: '';
            width: 60px;
            height: 3px;
            background-color: var(--highlight-color);
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
        }

        .philosophy {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 50px;
            text-align: center;
        }

        .philosophy p {
            font-size: 18px;
            color: #555;
            max-width: 900px;
            margin: 0 auto 20px;
        }

        .pillars {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 60px;
        }

        .pillar-card {
            background-color: white;
            padding: 30px 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-top: 4px solid var(--highlight-color);
            transition: transform 0.3s;
        }

        .pillar-card:hover {
            transform: translateY(-5px);
        }

        .pillar-card h3 {
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        /* Plan / Pricing Section */
        .pricing-section {
            background-color: #eef2f3;
            padding: 60px 20px;
        }

        .plan-box {
            background-color: white;
            max-width: 800px;
            margin: 0 auto;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            overflow: hidden;
            border: 1px solid #e1e8ed;
        }

        .plan-header {
            background: linear-gradient(to right, var(--primary-color), var(--accent-color));
            color: white;
            text-align: center;
            padding: 40px 20px;
        }

        .plan-header h3 {
            font-size: 28px;
            margin-bottom: 10px;
        }

        .price {
            font-size: 46px;
            font-weight: bold;
            color: var(--highlight-color);
        }

        .price span {
            font-size: 18px;
            color: #ddd;
        }

        .plan-features {
            padding: 40px;
        }

        .feature-item {
            margin-bottom: 25px;
            padding-left: 30px;
            position: relative;
        }

        .feature-item::before {
            content: '✓';
            color: var(--highlight-color);
            font-weight: bold;
            position: absolute;
            left: 0;
            top: 0;
            font-size: 18px;
        }

        .feature-item h4 {
            color: var(--primary-color);
            font-size: 18px;
            margin-bottom: 5px;
        }

        .feature-item p {
            color: #666;
            font-size: 15px;
        }

        /* Guarantees */
        .guarantees {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 50px;
        }

        @media (max-width: 768px) {
            .guarantees { grid-template-columns: 1fr; }
        }

        .guarantee-card {
            background: #fff8f5;
            border-left: 4px solid #ff6b6b;
            padding: 25px;
            border-radius: 0 8px 8px 0;
        }

        .guarantee-card.bonus {
            background: #f5fbe8;
            border-left: 4px solid #82c91e;
        }

        .guarantee-card h4 {
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        /* Contact Form / Action */
        .contact-section {
            background-color: white;
            padding: 60px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-top: 50px;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }

        @media (max-width: 768px) {
            .contact-grid { grid-template-columns: 1fr; }
        }

        .contact-info h3 {
            font-size: 26px;
            color: var(--primary-color);
            margin-bottom: 15px;
        }

        .contact-info p {
            margin-bottom: 20px;
            color: #555;
        }

        .info-details p {
            margin-bottom: 10px;
            font-weight: bold;
        }

        .info-details span {
            font-weight: normal;
            color: #666;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        input, textarea {
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            width: 100%;
        }

        textarea {
            height: 120px;
            resize: none;
        }

        /* Footer */
        footer {
            background-color: var(--primary-color);
            color: white;
            text-align: center;
            padding: 30px;
            margin-top: 60px;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">
            <h1>NEXARA <span>FINANCE</span></h1>
        </div>
        <div>
            <p style="font-size: 14px; opacity: 0.8;">Luz Dalia Granados Diaz | Directora</p>
        </div>
    </header>

    <section class="hero">
        <h2>El socio estratégico que tu Pyme necesita</h2>
        <p>Unimos la dirección financiera avanzada con Inteligencia Artificial para darte respuestas rápidas, claridad absoluta y resultados concretos.</p>
        <a href="#contacto" class="btn-cta">Agendar Sesión de Diagnóstico Gratis</a>
    </section>

    <main class="container">
        
        <section class="philosophy">
            <h2 class="section-title">Nuestra Filosofía</h2>
            <p>Gestionar un negocio ya es lo suficientemente complejo como para que también tengas que pelearte con los números a solas. Las gestorías tradicionales suelen limitarse a registrar el pasado y presentar impuestos cuando ya es poco lo que se puede hacer.</p>
            <p><strong>En Nexara Finance cambiamos las reglas:</strong> no somos un banco ni una gestoría común. Somos tu socio financiero estratégico y una mano amiga fiable en la que puedes apoyarte para tomar cada decisión importante.</p>
        </section>

        <section class="pillars">
            <div class="pillar-card">
                <h3>Claridad</h3>
                <p>Sin jerga financiera aburrida. Hablamos tu mismo idioma.</p>
            </div>
            <div class="pillar-card">
                <h3>Confianza</h3>
                <p>Soluciones basadas en datos y resultados reales y medibles.</p>
            </div>
            <div class="pillar-card">
                <h3>Agilidad</h3>
                <p>Respuestas y decisiones rápidas, porque tu tiempo es dinero.</p>
            </div>
            <div class="pillar-card">
                <h3>Cercanía</h3>
                <p>Trato directo, personalizado y empático con un experto a tu lado.</p>
            </div>
        </section>

    </main>

    <section class="pricing-section">
        <div class="container" style="padding-top:0; padding-bottom:0;">
            <h2 class="section-title">Nuestra Propuesta</h2>
            
            <div class="plan-box">
                <div class="plan-header">
                    <h3>PLAN AVANZADO AI-DRIVEN</h3>
                    <p>Delega el control de tus finanzas y gana una CFO de confianza</p>
                    <div class="price">450 € <span>/ mes</span></div>
                </div>
                
                <div class="plan-features">
                    <div class="feature-item">
                        <h4>Consultoría Estratégica, Viabilidad y Ventajas</h4>
                        <p>Analizamos la viabilidad de tus proyectos (maquinaria, personal, líneas de negocio) y diseñamos la estrategia que mejor posicione a tu empresa.</p>
                    </div>
                    <div class="feature-item">
                        <h4>Auditoría Preventiva de Impuestos con IA</h4>
                        <p>Utilizamos Inteligencia Artificial avanzada para simular inspecciones de Hacienda, detectar alertas de riesgo y descubrir deducciones fiscales antes de presentar tus borradores.</p>
                    </div>
                    <div class="feature-item">
                        <h4>Planificación, Dirección Financiera y Tesorería</h4>
                        <p>Monitoreamos tu caja mensualmente para maximizar tu liquidez y optimizar tus costes con un plan real y estratégico.</p>
                    </div>
                    <div class="feature-item">
                        <h4>Gestión Activa de Financiación</h4>
                        <p>Buscamos, filtramos y gestionamos las mejores opciones de capital, ayudas y líneas de crédito bancarias.</p>
                    </div>

                    <div class="guarantees">
                        <div class="guarantee-card">
                            <h4>Mes de Diagnóstico Cero Riesgo</h4>
                            <p>Si en los primeros 30 días no identificamos al menos una fuga de dinero o una oportunidad de ahorro equivalente al coste de nuestro servicio, <strong>te devolvemos el 100% de tu dinero</strong>.</p>
                        </div>
                        <div class="guarantee-card bonus">
                            <h4>Bono de Atención Extraordinaria</h4>
                            <p>Premiamos tu compromiso. Facilítanos tus cierres y facturas dentro de los 3 primeros días del mes y recibe un <strong>5% de descuento directo</strong>.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
<section class="container" id="contacto">
    <div class="contact-section">
        <div class="contact-grid">
            <div class="contact-info">
                <h3>¿Damos el primer paso?</h3>
                <p style="font-style: italic; font-size: 18px; color: var(--accent-color);">"Sabemos que gestionar las finanzas no es lo tuyo. Es el nuestro."</p>
                <p>Deja atrás la incertidumbre y comencemos a impulsar tu negocio hoy mismo agendando una sesión completamente gratuita.</p>
                
                <div class="info-details">
                    <p>👉 Teléfono: <span>+34 616 116 893</span></p>
                    <p>👉 Email: <span>gestiongranados@gmail.com</span></p>
                    <p>👉 Web Oficial: <span>nexarafinance.com/consulta-gratuitas</span></p>
                </div>
            </div>
            
            <div>
                <h4 style="margin-bottom: 15px; color: var(--primary-color);">Solicitar Sesión de Diagnóstico</h4>
                
                <!-- Formulario conectado a la función JavaScript -->
                <form onsubmit="handleSubmit(); return false;" id="lead-form">
                    <div id="form-fields">
                        <input type="text" id="nombre" placeholder="Nombre de la Pyme / Tu Nombre" required>
                        <input type="email" id="email" placeholder="Tu Correo Electrónico" required>
                        <input type="tel" id="telefono" placeholder="Tu Teléfono de Contacto" required>
                        <input type="text" id="empresa" placeholder="Nombre de tu Empresa (Opcional)">
                        <input type="text" id="sector" placeholder="Sector de tu Pyme">
                        <textarea id="mensaje" placeholder="Cuéntanos brevemente sobre tu negocio o qué necesitas optimizar..."></textarea>
                        <button type="submit" class="btn-cta form-submit" style="border-radius: 4px;">SÍ, QUIERO AGENDAR MI SESIÓN GRATUITA</button>
                    </div>
                </form>
                
                <!-- Mensaje de éxito que aparecerá al enviar -->
                <div id="form-success" style="display: none; color: #185FA5; margin-top: 15px; font-weight: bold; font-family: Inter, sans-serif;">
                    ¡Gracias por tu interés! Tu solicitud ha sido registrada con éxito. Luz Dalia se pondrá en contacto contigo a la brevedad.
                </div>
            </div>
        </div>
    </div>
</section>

<footer>
    <p>&copy; 2026 Nexara Finance - Tu crecimiento, nuestra dirección.</p>
    <p style="opacity: 0.6; font-size: 12px; margin-top: 5px;">Propuesta Comercial de Servicios Financieros Premium</p>
</footer>

<!-- FUNCIÓN TECNOLÓGICA QUE CONECTA CON TU WEBHOOK DE MAKE -->
<script>
function handleSubmit() {
  const nombre = document.getElementById('nombre').value.trim();
  const email = document.getElementById('email').value.trim();
  const telefono = document.getElementById('telefono').value.trim();
  const empresa = document.getElementById('empresa').value.trim();
  const sector = document.getElementById('sector').value.trim();
  const mensaje = document.getElementById('mensaje').value.trim();

  // Feedback visual en el botón para el usuario
  const btn = document.querySelector('.form-submit');
  const originalText = btn.innerText;
  btn.innerText = 'Enviando...';
  btn.disabled = true;

  // REEMPLAZA ESTA URL DE EJEMPLO POR LA URL REAL QUE COPIASTE EN TU PANE DE MAKE
  const webhookUrl = 'https://hook.eu1.make.com/ztx3efdqhji29susmxt6yh5bf8uefo40';

  fetch(webhookUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      nombre: nombre,
      email: email,
      telefono: telefono,
      empresa: empresa,
      sector: sector,
      mensaje: mensaje,
      fecha: new Date().toISOString()
    })
  })
  .then(() => {
    // Ocultar campos y mostrar mensaje de éxito corporativo
    document.getElementById('form-fields').style.display = 'none';
    document.getElementById('form-success').style.display = 'block';
  })
  .catch((error) => {
    console.error('Error:', error);
    alert('Hubo un problema al procesar tu solicitud. Por favor, inténtalo de nuevo.');
    btn.innerText = originalText;
    btn.disabled = false;
  });
}
</script>

</body>
</html>
