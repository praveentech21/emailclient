import base64
import json
from feedback import feedbackcode
from mailauthcate import mailauthenticate
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def send_email(to_address, subject):
    creds = mailauthenticate()
    # response_content = get_responce(classfi)
    # feedback_content = feedbackcode(subject, body, to_address, response_content)
    feedback_content = """
    <!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<title></title>
<!--[if !mso]><!-- -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<!--<![endif]-->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style type="text/css">#outlook a { padding:0; }
          body, .body { margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%; }
          table { border-spacing:0;}
          img { border:0;height:auto;line-height:100%; outline:none;text-decoration:none;-ms-interpolation-mode:bicubic; }
          p { display:block;margin:13px 0; }</style>

<link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
<link href="https://client-data.knak.io/production/company_data/5e501bf6edcaa/custom-fonts/6011caa83bb3f/fonts.css" rel="stylesheet" type="text/css">
<link href="https://assets.knak.io/custom-fonts/Helvetica/Helvetica.css" rel="stylesheet" type="text/css">
<style type="text/css">@import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
@import url(https://client-data.knak.io/production/company_data/5e501bf6edcaa/custom-fonts/6011caa83bb3f/fonts.css);

@import url(https://assets.knak.io/custom-fonts/Helvetica/Helvetica.css);</style>
<!--<![endif]-->
<style type="text/css">@media only screen and (min-width:480px) {
        .mj-column-per-100 { width:100% !important; max-width: 100%; }
.mj-column-per-44 { width:44% !important; max-width: 44%; }
.mj-column-per-9 { width:9% !important; max-width: 9%; }
.mj-column-per-22 { width:22% !important; max-width: 22%; }
.mj-column-per-25 { width:25% !important; max-width: 25%; }
.mj-column-per-55 { width:55% !important; max-width: 55%; }
.mj-column-per-45 { width:45% !important; max-width: 45%; }
.mj-column-per-50 { width:50% !important; max-width: 50%; }
.mj-column-per-24 { width:24% !important; max-width: 24%; }
.mj-column-per-33 { width:33% !important; max-width: 33%; }
.mj-column-per-43 { width:43% !important; max-width: 43%; }
      }</style>
<style type="text/css">u ~ div ul, u ~ div ol {margin-left: -3px}
.links-0068A5-underline a { color: #0068A5; text-decoration: underline; }
[x-apple-data-detectors-type] { 
          color: inherit !important; 
          -webkit-text-decoration-color: inherit !important; 
          text-decoration: inherit !important;
          font-weight: inherit !important;
         }
.links-67788A-underline a { color: #67788A; text-decoration: underline; }
        

        
            @media only screen and (min-width:480px) {        
                .img-full-width { max-width: 100% !important}
            }</style>
<style type="text/css">p{margin: 0 0;}ul{display: block;}ul li{list-style: disc;}li li{list-style: circle;}sup, sub{line-height:0;}body a{text-decoration: none; color: #0068A5;}.image-highlight{transition: 0.3s;}.image-highlight:hover{filter: brightness(1.2);}.button-highlight{transition: 0.3s;}.button-highlight:hover{filter: brightness(1.5);}@media only screen and (min-width: 480px) { .hide-on-mobile{display:block !important;}.hide-on-desktop{display:none !important;} }.hide-on-desktop{display:block;}.hide-on-mobile{display:none;}</style>

<style>[class~="x_body"] { width: 99.9% }</style>
</head>
<body style="word-spacing:normal;background-color:#FFFFFF;" class="body">
<img src="https://content.atmeta.com/trk?t=1&mid=MjY3LVBWQi05NDEAAAGPMB9ddnaZ3LD6tACvUfiHIS6QnkZbFClmMxq3g-NWaEEKBbs4rXWTHeA7qB13bVRozpWsYwyVefARYPYIoMYHtdl4amZrqk3d50fIKovxIrHAaGqdGyoiMNUKq_wo5602oHYGYHsaZ1Dv7Tu8AKt-qFJSu_nJ" width="1" height="1" style="display:none !important;" alt="" />

<!--[if !mso 9]><!-->
<div id="emailPreHeader" class="mktEditable" style="display: none;">
Boost engagement and drive awareness of your app with Instagram Reels
</div>
<div style="display: none;">
 ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏  ͏ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ &nbsp;
</div>
<!--<![endif]-->
<div style="background-color:#FFFFFF;background-position:center center;background-size:auto;background-repeat:repeat;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="hide-on-mobile-outlook block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#FFFFFF;background-color:#FFFFFF;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;width:100%;">
<tbody>
<tr>
<td style="display: none; font-size: 0px; padding: 25px 0 25px 0; text-align: center; vertical-align: top;" class="hide-on-mobile block-grid" align="center" valign="top">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
<div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;vertical-align:top;">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:352px;" ><![endif]-->
<div class="mj-column-per-44 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:44%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:middle;" width="100%">
<tbody>
<tr>
<td style="font-size:0px;padding:0 0 0 0;word-break:break-word;">
<div style="line-height:20px;height:20px;mso-line-height-alt:20px;">
&nbsp;
</div></td>
</tr>
<tr>
<td class="img-container" style="font-size:0px;padding:0px 0px 0px 26px;word-break:break-word;text-align:left;">
<div style="margin:0 auto 0 0;max-width:277px;">
<div class="mktoImg" id="kimage-5zzg9rkus" mktolockimgsize="true" mktolockimgstyle="true">
<a href=
"https://content.atmeta.com/dcn/YaB9AEmQPoKwP0sZ5nSiONPnpmAcD9SYYN_RNe4II41-TAyErDuJJI5tGJejYHYy23Kh6sifLLcsK3Qpj86vbSB7wZ4fO1CeII2YqwTywLWU62aB3CA5g4vby-IG8E007KGq8Ry4TEZkMtXm7VGcmihzJbqsXUTbJAEjQAC6P8y0JCrk2jv5aiXqzazMxBUREqomPjEXoeJX9k1mM42Ik33XFVsUmUNGEcdFDFiecTgySSNCGpCKdwscaSioKdVcqxNiTFL9XZyVnYZiHpwyybnGyKk5hiOi6vRFcgJBQNY=/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img height="auto" width="277" src="https://client-data.knak.io/production/email_assets/5e501bf6edcaa/iwCAs4GShKFDjjWfeTO2ezJWj5xOYaoDiQKg31qg.webp" style="border:none;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;display:block;"></a>
</div>
<!--[if !mso 9]><!-->
<div class="mktEditable" id="image-plain-text-bwib6oa8l" style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
[ Image ] [[https://developers.facebook.com/?content_id=Bgj0xC2MyPjbUsu&utm_source=email&utm_medium=m4d-str-nov23&utm_campaign=organic&utm_offering=developer-platform&utm_product=platform&utm_content=footer-fb4d&utm_location=9]]
</div>
<!--<![endif]-->
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:middle;width:72px;" ><![endif]-->
<div class="mj-column-per-9 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:9%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:middle;" width="100%"></table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:middle;width:176px;" ><![endif]-->
<div class="mj-column-per-22 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:22%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:middle;" width="100%">
<tbody>
<tr>
<td style="font-size:0px;padding:0 0 0 0;word-break:break-word;">
<div style="line-height:20px;height:20px;mso-line-height-alt:20px;">
&nbsp;
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:middle;width:200px;" ><![endif]-->
<div class="mj-column-per-25 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:25%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:middle;" width="100%">
<tbody>
<tr>
<td style="font-size:0px;padding:0 0 0 0;word-break:break-word;">
<div style="line-height:20px;height:20px;mso-line-height-alt:20px;">
&nbsp;
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]-->
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
<!--[if !mso]><!-->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="hide-on-desktop-outlook block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#FFFFFF;background-color:#FFFFFF;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;width:100%;">
<tbody>
<tr>
<td style="display: block; font-size: 0px; padding: 0px 0px 25px 0px; text-align: center; vertical-align: top;" class="hide-on-desktop block-grid" align="center" valign="top">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
<div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;vertical-align:top;">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:440px;" ><![endif]-->
<div class="mj-column-per-55 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:55%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%">
<tbody>
<tr>
<td class="img-container" style="font-size:0px;padding:40px 0px 0px 40px;word-break:break-word;text-align:center;">
<div style="margin:0 auto;max-width:400px;" class="img-full-width">
<div class="mktoImg" id="kimage-7ycymbi9g" mktolockimgsize="true" mktolockimgstyle="true">
<a href=
"https://content.atmeta.com/dcn/YaB9AEmQPoKwP0sZ5nSiONPnpmAcD9SYYN_RNe4II41-TAyErDuJJI5tGJejYHYy23Kh6sifLLcsK3Qpj86vbSB7wZ4fO1CeII2YqwTywLWU62aB3CA5g4vby-IG8E007KGq8Ry4TEZkMtXm7VGcmihzJbqsXUTbJAEjQAC6P8y0JCrk2jv5aiXqzazMxBUREqomPjEXoeJX9k1mM42Ik33XFVsUmUNGEcdFDFiecTgySSNCGpCKdwscaSioKdVcqxNiTFL9XZyVnYZiHpwyybnGyKk5hiOi6vRFcgJBQNY=/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img alt="Meta for Developers" height="auto" width="400" src="https://client-data.knak.io/production/email_assets/5e501bf6edcaa/sz9qxHovphpe1ghEDWpLEOX3Aiqe0BVCFhZ8UhU9.webp" style="border:none;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;display:block;"></a>
</div>
<!--[if !mso 9]><!-->
<div class="mktEditable" id="image-plain-text-kwnwbp39k" style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
[ Meta for Developers ] [[https://developers.facebook.com/?content_id=Bgj0xC2MyPjbUsu&utm_source=email&utm_medium=m4d-str-nov23&utm_campaign=organic&utm_offering=developer-platform&utm_product=platform&utm_content=footer-fb4d&utm_location=9]]
</div>
<!--<![endif]-->
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:top;width:360px;" ><![endif]-->
<div class="mj-column-per-45 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:45%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%"></table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]-->
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
<!--<![endif]-->
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#FFFFFF;background-color:#FFFFFF;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;width:100%;">
<tbody>
<tr>
<td style="font-size:0px;padding:0;text-align:center;vertical-align:top;" class="block-grid">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
<div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%">
<tbody>
<tr>
<td class="img-container" style="font-size:0px;padding:20px 32px 0px 32px;word-break:break-word;text-align:center;">
<div style="margin:0 auto;">
<div class="mktoImg" id="kimage-84osmwtem" mktolockimgsize="true" mktolockimgstyle="true">
<a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9dduA83bgOeev1407t9_4MAodSjcEUoeOaFINvnd41fCfYcioZ_bqQLOrfLLQAgppyrNA=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img height="auto" width="736" src="https://client-data.knak.io/production/email_assets/5e501bf6edcaa/AFKxJmHeRaVSoQ7SJKAna41VTjLalDhWdfSIpAot.jpg" style="border:none;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;display:block;"></a>
</div>
<!--[if !mso 9]><!-->
<div class="mktEditable" id="image-plain-text-uwpi6n79z" style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
[ Image ] [[https://developers.facebook.com/success-stories/smule/?content_id=cOnBw5zJ5yjoqFd]]
</div>
<!--<![endif]-->
</div></td>
</tr>
<tr>
  <td style="font-size:0px;padding:0;text-align:center;vertical-align:top;" class="block-grid">
  <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
  <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%">
  <tbody>
  <tr>
  <td class="img-container" style="font-size:0px;padding:20px 32px 0px 32px;word-break:break-word;text-align:center;">
  <div style="margin:0 auto;">
  <div class="mktoImg" id="kimage-84osmwtem" mktolockimgsize="true" mktolockimgstyle="true">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/GGTorJjJq-c?si=nzIj02Y04VOBL-aq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  <!--[if !mso 9]><!-->
  <div class="mktEditable" id="image-plain-text-uwpi6n79z" style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
  [ Image ] [[https://developers.facebook.com/success-stories/smule/?content_id=cOnBw5zJ5yjoqFd]]
  </div>
  <!--<![endif]-->
  </div></td>
  </tr>
  
<tr>
<td class="text-container" style="font-size:0px;padding:26px 32px 0px 32px;word-break:break-word;text-align:left;">
<div class="mktEditable" id="ktext-i3zp9uvdr" style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:16px;letter-spacing:none;line-height:1.8;text-align:left;mso-line-height-alt:1.813em;color:#414141;">
<div class="links-0068A5-underline"> 
<div style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:16px;letter-spacing:none;line-height:1.8;text-align:left;mso-line-height-alt:1.813em;color:#414141;"> 
<p style="margin: 0 0;"><em>“Since launching Sharing to Reels, we’ve seen a major boost in sharing activity on Facebook and Instagram and overwhelmingly positive reactions from our community.” &nbsp;</em><br><em>-Kevin Carson, SVP Global Artist and Industry Relations at Smule</em></p> 
<p style="margin: 0 0;">&nbsp;</p> 
<p style="margin: 0 0;">Enabling <a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddtadOfb4B6_Z68ee3OBpJZHQb6xK1YP982oND43OPCSrJ0AOwDFdgBp7Dy_5QSRo7hw=" target="_blank" rel="noopener" style="color: rgb(0, 104, 165); text-decoration: underline;"
>Sharing to Reels</a> makes it easy for people to share short-form videos directly to Instagram Reels from your app, where they can reach a wider audience and increase awareness of your app at the same time.&nbsp;</p> 
<p style="margin: 0 0;">&nbsp;</p> 
<p style="margin: 0 0;"><strong>Why Should You Integrate With Sharing to Reels on Instagram?</strong></p> 
<ul style="display: block; margin-top: 0; margin-bottom: 0; padding-left: 40px; mso-para-margin-left: 40px;"> 
<li style="list-style: disc; margin: 0; margin-top: 1em;"><strong>Increase Brand Awareness:</strong> Sharing videos from your app to Reels can boost brand awareness and organic traffic. Find out how a <a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddib-n09b8OaAHFJrUfxVAZVFoV2kSaXhxB0V58ESnPiaH464TtDzmEWQKu3avfjLm2c=" target="_blank" rel="noopener" style="color: rgb(0, 104, 165); text-decoration: underline;"
>150% increase in shared content helped Smule (one of the most popular social music apps) earn more organic traffic after integrating with Sharing to Reels.</a></li> 
<li style="list-style: disc; margin: 0;"><strong>Self-serve implementation:</strong> With self-serve documentation (<a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddjVuAzvRbECad675nKuySvUE--aqxBEOIwoqgwRUDPjHkF8hGRXJEQq6XV5pM_cho0E=" target="_blank" rel="noopener" style="color: rgb(0, 104, 165); text-decoration: underline;"
>iOS</a>; <a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddtl8ZCAmtql8dXnnsDOYSjxrpLvsiBENB6SgL_qxKn419TK3q49wyQ_n5Xc8endd2ew=" target="_blank" rel="noopener" style="color: rgb(0, 104, 165); text-decoration: underline;"
>Android</a>), you can implement Sharing to Reels on Instagram within weeks, or even days for simpler integration setups.</li> 
<li style="list-style: disc; margin: 0; margin-bottom: 1em;"><strong>Provide Value to Your Users:</strong> Your users can now share content directly to Instagram Reels with a convenient sharing, saving them time and making sharing more accessible than ever.</li> 
</ul> 
<p style="margin: 0 0;">&nbsp;</p> 
<p style="margin: 0 0;"><strong>Ready to Integrate?&nbsp;</strong><br>Review our documentation to get started with Sharing to Reels today!</p> 
<p style="margin: 0 0;">&nbsp;</p> 
</div> 
</div>
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#FFFFFF;background-color:#FFFFFF;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;width:100%;">
<tbody>
<tr>
<td style="font-size:0px;padding:0px;text-align:center;vertical-align:top;" class="block-grid">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
<div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%">
<tbody>
<tr>
<td style="font-size:0px;padding:0 0 0 0;word-break:break-word;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:13px;line-height:1;width:100%;">
<tbody>
<tr>
<td style="vertical-align:top;">
<table border="0" cellpadding="0" cellspacing="0" style="min-width:600px" width="600">
<tbody>
<tr>
<td width="100%">
<div style="mso-hide:all;visibility:hidden;opacity:0;color:transparent;mso-line-height-rule:exactly;line-height:0;font-size:0px;overflow:hidden;border-width:0;display:none">
<a href="https://go.atmeta.com/UnsubscribePage.html?mkt_unsubscribe=1&mkt_tok=MjY3LVBWQi05NDEAAAGPMB9ddnnrEhMfm0AJCPpwe1Ud46czbl2rR4QswN8FKJA-U2qFM3JZQLobXQGBAiGZ887n6kfU95z6rTeBae1ANUMEx5KvWarABnXrjFVPdO0Y9NgSwVk" style="text-decoration: none; display: none; font-size: 0; color: transparent;"></a>
</div></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#FFFFFF;background-color:#FFFFFF;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;width:100%;">
<tbody>
<tr>
<td style="font-size:0px;padding:0px;text-align:center;vertical-align:top;" class="block-grid">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:400px;" ><![endif]-->
<div class="mj-column-per-50 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%">
<tbody>
<tr>
<td valign="middle" class="button-container" style="font-size:0px;padding:10px 25px 10px 25px;word-break:break-word;text-align:center;">
<div>
<!--[if mso]><table width="100%" align="center" border="0" cellpadding="0" cellspacing="0" style="border-spacing:0;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;"><tr><td align="center" class="mso-button-dark-mode"><a:roundrect xmlns:a="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddhRYSr_O1EhQ3p2kcZlqQlPutpibThv8pjSs2KXFkBYRMvfLp6Ys5NsUe-Gs5rBq-zY=" fillcolor="#FFFFFF" arcsize="66%" style="v-text-anchor:middle;width:60pt;height:28.5pt;" strokecolor="#000000" strokeweight="0.75pt" 
><w:anchorlock/><a:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:sans-serif, Arial; font-size:16px" class="mso-text-black"><![endif]--> 
<a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddhRYSr_O1EhQ3p2kcZlqQlPutpibThv8pjSs2KXFkBYRMvfLp6Ys5NsUe-Gs5rBq-zY=" style="display: inline-block; background: #FFFFFF; color: #000000; font-family: 'Optimistic Text', Helvetica, sans-serif; font-size: 16px; font-weight: bold; line-height: 1; margin: 0; text-align: center; text-decoration: none; text-transform: none; padding: 10px 25px 10px 25px; mso-padding-alt: 0px; border-radius: 25px; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; border-bottom: 1px solid #000000; mso-border-alt: none; box-sizing: border-box;" target="_blank" width="80"
><strong>iOS</strong> </a>
<!--[if mso]></center></a:textbox></a:roundrect></td></tr></table><![endif]-->
<!--[if !mso 9]><!-->
<div class="mktEditable" id="button-plain-text-pogk2gcmj" style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
iOS [[https://developers.facebook.com/docs/ios/sharing-to-reels-instagram?content_id=Xg31PAPnuti2HoI]]
</div>
<!--<![endif]-->
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:top;width:400px;" ><![endif]-->
<div class="mj-column-per-50 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:top;" width="100%">
<tbody>
<tr>
<td valign="middle" class="button-container" style="font-size:0px;padding:10px 25px 10px 25px;word-break:break-word;text-align:center;">
<div>
<!--[if mso]><table width="100%" align="center" border="0" cellpadding="0" cellspacing="0" style="border-spacing:0;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;"><tr><td align="center" class="mso-button-dark-mode"><a:roundrect xmlns:a="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddoIc77mQzP7DF2WI4uiqXYqYeKGydzxkoc7SsWmodaO4JAhyTzOfP0ETKvgr6IZ4NrQ=" fillcolor="#FFFFFF" arcsize="66%" style="v-text-anchor:middle;width:85.5pt;height:28.5pt;" strokecolor="#000000" strokeweight="0.75pt" 
><w:anchorlock/><a:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:sans-serif, Arial; font-size:16px" class="mso-text-black"><![endif]--> 
<a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddoIc77mQzP7DF2WI4uiqXYqYeKGydzxkoc7SsWmodaO4JAhyTzOfP0ETKvgr6IZ4NrQ=" style="display: inline-block; background: #FFFFFF; color: #000000; font-family: 'Optimistic Text', Helvetica, sans-serif; font-size: 16px; font-weight: bold; line-height: 1; margin: 0; text-align: center; text-decoration: none; text-transform: none; padding: 10px 25px 10px 25px; mso-padding-alt: 0px; border-radius: 25px; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; border-bottom: 1px solid #000000; mso-border-alt: none; box-sizing: border-box;" target="_blank" width="114"
><strong>Android</strong> </a>
<!--[if mso]></center></a:textbox></a:roundrect></td></tr></table><![endif]-->
<!--[if !mso 9]><!-->
<div class="mktEditable" id="button-plain-text-kcixzgmz8" style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
Android [[https://developers.facebook.com/docs/android/sharing-to-reels-instagram?content_id=8k8nwbCxzQ5weCP]]
</div>
<!--<![endif]-->
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#F5F6F6;background-color:#F5F6F6;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F6F6;width:100%;">
<tbody>
<tr>
<td style="font-size:0px;padding:10px 0px 0px 24px;text-align:center;vertical-align:top;" class="block-grid">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:bottom;width:186.24px;" ><![endif]-->
<div class="mj-column-per-24 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:bottom;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:bottom;" width="100%">
<tbody>
<tr>
<td class="text-container" style="font-size:0px;padding:5px 35px 5px 2px;word-break:break-word;text-align:left;">
<div class="mktEditable" id="ktext-tu8mlkuka" style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:12px;letter-spacing:none;line-height:1.2;text-align:left;mso-line-height-alt:0.875em;color:#67788A;">
<div class="links-0068A5-underline"> 
<div style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:12px;letter-spacing:none;line-height:1.2;text-align:left;mso-line-height-alt:0.875em;color:#67788A;"> 
<p style="margin: 0 0;">Stay connected</p> 
</div> 
</div>
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:bottom;width:256.08px;" ><![endif]-->
<div class="mj-column-per-33 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:bottom;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:bottom;" width="100%">
<tbody>
<tr>
<td class="text-container" style="font-size:0px;padding:5px 35px 5px 2px;word-break:break-word;text-align:left;">
<div class="mktEditable" id="ktext-aw0khqxwi" style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:12px;letter-spacing:none;line-height:1.2;text-align:left;mso-line-height-alt:0.875em;color:#67788A;">
<div class="links-67788A-underline"> 
<div style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:12px;letter-spacing:none;line-height:1.2;text-align:left;mso-line-height-alt:0.875em;color:#67788A;"> 
<p style="margin: 0 0;"><a href=
"https://content.atmeta.com/dcn/YaB9AEmQPoKwP0sZ5nSiONPnpmAcD9SYYN_RNe4II42Lqv3sb2tsZj71rQHZ7nRS5whTYMEf3EhS3jtrKBjCN01D9s2hCGMHQvMr0sBr0Y2hRc9ojc1RaB2398Emj9z_bauqx4Jm1x29mSLvFNmOJs3NmbhVR3K-9AEQvUT50eRBBUsHylxNLs0bWcDjcoaKRyGTge5rAkOXEpRBvYW1K9oO22W0JpeZ0ukGN9xiKr2tqjWl9PNoVhsJrmgvXdxIXKvsuzjWIcyxbm8Qbr7_nmJnwczJuhpc-njmeog14Xs=/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" rel="noopener" style="color: rgb(103, 120, 138); text-decoration: underline;"
>developers.meta.com</a></p> 
</div> 
</div>
</div></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td style="vertical-align:bottom;width:333.68px;" ><![endif]-->
<div class="mj-column-per-43 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:bottom;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:bottom;" width="100%">
<tbody>
<tr>
<td class="social-container" style="font-size:0px;padding:10px 0px 0px 0px;word-break:break-word;text-align:left;">
<!--[if mso | IE]><table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" ><tr><td><![endif]-->
<div style="display:inline-block;">
<table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
<tbody>
<tr>
<td style="padding:6px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;border-radius:0px;width:22px;">
<tbody>
<tr>
<td style="padding:0px;font-size:0;height:22px;vertical-align:middle;width:22px;">
<div class="mktEditable" id="ksocial-9xc6ng7h3">
<a href=
"https://content.atmeta.com/dcn/uq3EykqQY7h0Yyhe2BWhMP1-41CRbllG_R2s5AIK2m-61_oFGEXKEuTnpGB7ys5z4wRtM4I5wwHTy3CwWTSE_nGb8OEC3Ndg6kb0eIieZHBmIDjiSk54yQFE4Z3e187D7DcGEULMuJh_Gpqn3XLHJ9BW14LrDXOi4mRO8hjm0WVZgDJFSN1SmxwDJZCIJujwtPeqHU2nqnSh0o_NPlcnS3igjphucILqiybSbjv3QT6HBSnDGP1Qg-O9KWvdyDYSYekM_LpH_IKRtYtFW5Xi8DFc1FB6H_H50DN95SD5RfQ=/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img alt="Facebook" height="22" src="https://go.facebookinc.com/rs/267-PVB-941/images/f4d-icon-facebook-20x20-2x.png" style="border-radius:0px;display:block;" width="22"></a>
</div></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td><![endif]-->
<div style="display:inline-block;">
<table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
<tbody>
<tr>
<td style="padding:6px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;border-radius:0px;width:22px;">
<tbody>
<tr>
<td style="padding:0px;font-size:0;height:22px;vertical-align:middle;width:22px;">
<div class="mktEditable" id="ksocial-73axkfz49">
<a href=
"https://content.atmeta.com/dcn/qRrMJDEUlv6ss-mBIC1z6mf8g-GyPzKfeDM_d_GSs3OD6HB5aZOcgoyETgQpPhcMTp5t_sEBjHXflzOBx9tL8AhHEpZ04M2eG4Y5oypLKKm90Y2-R-ILOHSCcYnKhTGAF6YQTdpjUixaC882RlwA091BhqMEpRUCmPL2d4SAvad2rddBY7sePTH9YGcYWvg1CvAM_Bn-6GYpmBbJB8GTX0CUCSFTHB41zoZd92rAKqbTx6EAKYUOEw6MG9j1ymNHsOSgEFLaFk3sMrwOZIFuJZY17JsWntoFw6u-BKjEfr0=/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img alt="Twitter" height="22" src="https://go.facebookinc.com/rs/267-PVB-941/images/f4d-icon-twitter-20x20-2x.png" style="border-radius:0px;display:block;" width="22"></a>
</div></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td><![endif]-->
<div style="display:inline-block;">
<table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
<tbody>
<tr>
<td style="padding:6px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;border-radius:0px;width:22px;">
<tbody>
<tr>
<td style="padding:0px;font-size:0;height:22px;vertical-align:middle;width:22px;">
<div class="mktEditable" id="ksocial-srgh3hfx3">
<a href=
"https://content.atmeta.com/dcn/WhZcq50CsoLLiaLsfDq43ooolxdO-A-84C7Uw-ExvXhGtr_OIYrxntuDhmSJQ7aeJnfRAmtF3X874zO1UqCDjlhGwR8_swel6_xZjWdMWCIJjt-kBNN-qK_cm-vyvt30SPpvf7E2LMYBMwl-6Y7JmUm423ZGYYyz35UQnJUyl2L3Rkxmr6yDJyCk0fI9W-vwNWcQzc01VuI9diGIo4YdLqepQEbEDhd5jIQuW7kymAClOnAyPCFJSjZJtOKCiOW1SCcCH_fwqlcpIpLizYJ5TI_TKpcl99HNZpQ-S5VhQX5rmOrgZUeKDpbS1evLn54d/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img alt="Instagram" height="22" src="https://go.facebookinc.com/rs/267-PVB-941/images/f4d-icon-instagram-20x20-2x.png" style="border-radius:0px;display:block;" width="22"></a>
</div></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td><![endif]-->
<div style="display:inline-block;">
<table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
<tbody>
<tr>
<td style="padding:6px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;border-radius:0px;width:22px;">
<tbody>
<tr>
<td style="padding:0px;font-size:0;height:22px;vertical-align:middle;width:22px;">
<div class="mktEditable" id="ksocial-cg2znq8d6">
<a href=
"https://content.atmeta.com/dcn/fG5-PlwEnZR-IoSdwCtjInBOEnkCOl-88iHvoC1GNZx7nuH0-lQyl4pqS_QlmKP8ychkFE9Y7-abFiN8nDF2ILrneY_V4UvnmF7Gp1QIdgSxFhGQVei5hS50fVmwOUfFZ3dkYwQVc9H5qdv0ykrtg4m7ov9ya7pwPotkP8EPsg8eqjLu5JITc2JePjMfBEfmqfE5JtlecI5-my6rmoIAiMByMD1uTPqZzM1P2iyuN0oILppi2_jHNXOhdI5VDfigljZQ8x6k3WtnDtUMRXTt6fnY5rnIM77GMh-jI_JVNiN-keZOjjkBdboN25oOb1sX/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img alt="Linkedin" height="22" src="https://go.facebookinc.com/rs/267-PVB-941/images/f4d-icon-linkedin-20x20-2x%20copy.png" style="border-radius:0px;display:block;" width="22"></a>
</div></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td><td><![endif]-->
<div style="display:inline-block;">
<table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:none;display:inline-table;">
<tbody>
<tr>
<td style="padding:6px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;border-radius:0px;width:22px;">
<tbody>
<tr>
<td style="padding:0px;font-size:0;height:22px;vertical-align:middle;width:22px;">
<div class="mktEditable" id="ksocial-sexfz5gbh">
<a href=
"https://content.atmeta.com/dcn/M9Y3nowLDCcEv8uSbJAkaa43shsysoPRvcP3h6mo5oPP6jStBhcNw_3HzWYyGRzph_IBgI041OjaITnI5gHZZZhAYx-Q0clSLd46Oe2d9EkErpIcAWQwCYcb0nMtgYo9z_bvfEwPFUSPQXmgFD3yoGZnYomvCJ_BM9Fu1lkKFoiO1ysyONG_HZwmxh3mkbIxmFWhOya91VsPcl-3X_hn_TJLi6J_CATYiXXADgz58sg9eL9JUWD7PfDJqnzVwNf853TXlUagTA5-fV8jJFXSnWnOE1OFtmwqMpteiMe8AUc=/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" style="text-decoration: none; color: #0068A5;"
><img alt="YouTube" height="22" src="https://go.facebookinc.com/rs/267-PVB-941/images/f4d-icon-youtube-20x20-2x%20copy.png" style="border-radius:0px;display:block;" width="22"></a>
</div></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F5F5;width:100%;" class="section">
<tbody>
<tr>
<td align="center">
<!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
<div style="background:#F5F6F6;background-color:#F5F6F6;Margin:0px auto;max-width:800px;">
<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#F5F6F6;width:100%;">
<tbody>
<tr>
<td style="font-size:0px;padding:0px 0px 15px 0px;text-align:center;vertical-align:top;" class="block-grid">
<!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:800px;" ><![endif]-->
<div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius:0px;vertical-align:middle;" width="100%">
<tbody>
<tr>
<td style="font-size:0px;padding:0 0 0 0;word-break:break-word;">
<div style="line-height:20px;height:20px;mso-line-height-alt:20px;">
&nbsp;
</div></td>
</tr>
<tr>
<td class="text-container" style="font-size:0px;padding:0px 26px 10px 26px;word-break:break-word;mso-padding-alt:0px 26px 10px 26px;text-align:left;">
<div class="mktEditable" id="ktext-a5rihtgv9" style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:12px;letter-spacing:none;line-height:1.4;text-align:left;mso-line-height-alt:1.063em;color:#67788A;">
<div class="links-67788A-underline"> 
<div style="font-family:'Optimistic Text', Helvetica, sans-serif;font-size:12px;letter-spacing:none;line-height:1.4;text-align:left;mso-line-height-alt:1.063em;color:#67788A;"> 
<p style="margin: 0 0;">© 2023 Meta. Meta Platforms, Inc., 1601 Willow Rd. Menlo Park, CA 94025 or where the Meta Products are offered to you by Meta Platforms Ireland Limited, 4 Grand Canal Square, Grand Canal Harbour, Dublin 2, Ireland</p> 
<p style="margin: 0 0;"><br><a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddhZyVwFkE8feRv3WE3QoiHTdla0tD98lLIeDR_rE6d3CQd8YR6eIM07N5PeItAVNjCE=" target="_blank" rel="noopener" style="color: rgb(103, 120, 138); text-decoration: underline;"
>Platform Policy</a> &nbsp; &nbsp; <a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddmLVg1r6-6MfNvrsxdH2rcO-HCkj-MXCOnamKdNnI-W6Y6KJGfXfbTMIYra3RzOGvTk=" target="_blank" rel="noopener" style="color: rgb(103, 120, 138); text-decoration: underline;"
>Privacy Policy</a> &nbsp; &nbsp; <a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddvWBDCpFD-72tr6mys158c9C4ad8P2V5FFXahn7ss28vN439y1s1OjNopHgwjLzZuUk=" target="_blank" rel="noopener" style="color: rgb(103, 120, 138); text-decoration: underline;"
>Terms</a> &nbsp; &nbsp; <a href=
"https://content.atmeta.com/dcn/uq3EykqQY7h0Yyhe2BWhMDrLtLNyk738gdtamPBcO_qWtL9fdXH1YnmT-TtXqJvqjLeBe4AtBY49c2ue-kt-B46b9_DvvCjG5RNbxbDsYWANyZqw1_lQzgyAMZCu0J60DQgJCtCegMF8D6bN9t1vPw==/MjY3LVBWQi05NDEAAAGPMB9ddgWElzUJN9W2Ff7SFQ9YdY8LKkMmjqG_GEi9TSrBJm8CmTbvZvwdPfIn2X5ymOX5-1Q=" target="_blank" rel="noopener" style="color: rgb(103, 120, 138); text-decoration: underline;"
>Unsubscribe</a></p> 
</div> 
</div>
</div></td>
</tr>
<tr>
<td style="font-size:0px;padding:0 0 0 0;word-break:break-word;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;width:100%;">
<tbody>
<tr>
<td style="vertical-align:top;">
<table border="0" cellpadding="0" cellspacing="0" class="m-shell" style="min-width:600px;" width="600">
<tbody>
<tr>
<td height="10" width="100%">
<!--[if !mso 9]><!-->
<div style="mso-hide:all; visibility:hidden; opacity:0; color:transparent; mso-line-height-rule:exactly; line-height:0; font-size:0px; overflow:hidden; border-width:0; display:none !important;">
<a href="https://go.atmeta.com/UnsubscribePage.html?mkt_unsubscribe=1&mkt_tok=MjY3LVBWQi05NDEAAAGPMB9ddnnrEhMfm0AJCPpwe1Ud46czbl2rR4QswN8FKJA-U2qFM3JZQLobXQGBAiGZ887n6kfU95z6rTeBae1ANUMEx5KvWarABnXrjFVPdO0Y9NgSwVk" style="text-decoration: none; display: none; font-size: 0; color: transparent;"></a>
</div>
<!--<![endif]--></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<!--[if mso | IE]></td></tr></table><![endif]--></td>
</tr>
</tbody>
</table>
</div>
<a href=
"https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddnjpptdIhp4dVuxepuIXG-pl3ulPplqeChnT9LIO6iUfwL2ZF6CnfAy2XA3vpDMPIPc="
></a></body>
</html>
    """
    
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(feedback_content, subtype="html")
        message["To"] = to_address
        message["From"] = "testpixeltest8@gmail.com"
        message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
        return send_message
    except HttpError as error:
        print(f"An error occurred: {error}")
        
send_email("ravikumar_csd@srkrec.edu.in", "Embaided HTML CODE IN GMAIL")
        
