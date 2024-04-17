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
    
    samplevariable = "This is a sample email"
    testingvariable = "This is a testing email"
    feedback_content = """
    <!DOCTYPE html>
<html
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
>
  <head>
    <title>pixeltest</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <style type="text/css">
      #outlook a {
        padding: 0;
      }

      body,
      .body {
        margin: 0;
        padding: 0;
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }

      table {
        border-spacing: 0;
      }

      img {
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
        -ms-interpolation-mode: bicubic;
      }

      p {
        display: block;
        margin: 13px 0;
      }
    </style>
    <link
      href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700"
      rel="stylesheet"
      type="text/css"
    />
    <link
      href="https://client-data.knak.io/production/company_data/5e501bf6edcaa/custom-fonts/6011caa83bb3f/fonts.css"
      rel="stylesheet"
      type="text/css"
    />
    <link
      href="https://assets.knak.io/custom-fonts/Helvetica/Helvetica.css"
      rel="stylesheet"
      type="text/css"
    />
    <style type="text/css">
      @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
      @import url(https://client-data.knak.io/production/company_data/5e501bf6edcaa/custom-fonts/6011caa83bb3f/fonts.css);

      @import url(https://assets.knak.io/custom-fonts/Helvetica/Helvetica.css);
    </style>
    <style type="text/css">
      @media only screen and (min-width: 480px) {
        .mj-column-per-100 {
          width: 100% !important;
          max-width: 100%;
        }

        .mj-column-per-44 {
          width: 44% !important;
          max-width: 44%;
        }

        .mj-column-per-9 {
          width: 9% !important;
          max-width: 9%;
        }

        .mj-column-per-22 {
          width: 22% !important;
          max-width: 22%;
        }

        .mj-column-per-25 {
          width: 25% !important;
          max-width: 25%;
        }

        .mj-column-per-55 {
          width: 55% !important;
          max-width: 55%;
        }

        .mj-column-per-45 {
          width: 45% !important;
          max-width: 45%;
        }

        .mj-column-per-50 {
          width: 50% !important;
          max-width: 50%;
        }

        .mj-column-per-24 {
          width: 24% !important;
          max-width: 24%;
        }

        .mj-column-per-33 {
          width: 33% !important;
          max-width: 33%;
        }

        .mj-column-per-43 {
          width: 43% !important;
          max-width: 43%;
        }
      }
    </style>
    <style type="text/css">
      u ~ div ul,
      u ~ div ol {
        margin-left: -3px;
      }

      .links-0068A5-underline a {
        color: #0068a5;
        text-decoration: underline;
      }

      [x-apple-data-detectors-type] {
        color: inherit !important;
        -webkit-text-decoration-color: inherit !important;
        text-decoration: inherit !important;
        font-weight: inherit !important;
      }

      .links-67788A-underline a {
        color: #67788a;
        text-decoration: underline;
      }

      @media only screen and (min-width: 480px) {
        .img-full-width {
          max-width: 100% !important;
        }
      }
    </style>
    <style type="text/css">
      p {
        margin: 0 0;
      }

      ul {
        display: block;
      }

      ul li {
        list-style: disc;
      }

      li li {
        list-style: circle;
      }

      sup,
      sub {
        line-height: 0;
      }

      body a {
        text-decoration: none;
        color: #0068a5;
      }

      .image-highlight {
        transition: 0.3s;
      }

      .image-highlight:hover {
        filter: brightness(1.2);
      }

      .button-highlight {
        transition: 0.3s;
      }

      .button-highlight:hover {
        filter: brightness(1.5);
      }

      @media only screen and (min-width: 480px) {
        .hide-on-mobile {
          display: block !important;
        }

        .hide-on-desktop {
          display: none !important;
        }
      }

      .hide-on-desktop {
        display: block;
      }

      .hide-on-mobile {
        display: none;
      }
    </style>
    <style>
      [class~="x_body"] {
        width: 99.9%;
      }
    </style>
  </head>

  <body style="word-spacing: normal; background-color: #ffffff" class="body">
    <img
      src="https://content.atmeta.com/trk?t=1&mid=MjY3LVBWQi05NDEAAAGPMB9ddnaZ3LD6tACvUfiHIS6QnkZbFClmMxq3g-NWaEEKBbs4rXWTHeA7qB13bVRozpWsYwyVefARYPYIoMYHtdl4amZrqk3d50fIKovxIrHAaGqdGyoiMNUKq_wo5602oHYGYHsaZ1Dv7Tu8AKt-qFJSu_nJ"
      width="1"
      height="1"
      style="display: none !important"
      alt
    />

    <!--[if !mso 9]><!-->
    <div id="emailPreHeader" class="mktEditable" style="display: none">
      Boost engagement and drive awareness of your app with Instagram Reels
    </div>
    <div style="display: none">
      ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏
      ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­ ­
      &nbsp;
    </div>
    <div
      style="
        background-color: #ffffff;
        background-position: center center;
        background-size: auto;
        background-repeat: repeat;
      "
    >
      <table
        align="center"
        border="0"
        cellpadding="0"
        cellspacing="0"
        role="presentation"
        style="background-color: #f5f5f5; width: 100%"
        class="section"
      >
        <tbody>
          <tr>
            <td align="center">
              <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="hide-on-mobile-outlook block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
              <div
                style="
                  background: #ffffff;
                  background-color: #ffffff;
                  margin: 0px auto;
                  max-width: 800px;
                "
              >
                <table
                  align="center"
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  role="presentation"
                  style="background-color: #ffffff; width: 100%"
                >
                  <tbody>
                    <tr>
                      <td
                        style="
                          display: none;
                          font-size: 0px;
                          padding: 25px 0 25px 0;
                          text-align: center;
                          vertical-align: top;
                        "
                        class="hide-on-mobile block-grid"
                        align="center"
                        valign="top"
                      >
                        <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
                        <div
                          class="mj-column-per-100 mj-outlook-group-fix"
                          style="
                            font-size: 0;
                            line-height: 0;
                            text-align: left;
                            display: inline-block;
                            width: 100%;
                            direction: ltr;
                            vertical-align: top;
                          "
                        >
                          <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:middle;width:352px;" ><![endif]-->
                          <div
                            class="mj-column-per-44 mj-outlook-group-fix"
                            style="
                              font-size: 0px;
                              text-align: left;
                              direction: ltr;
                              display: inline-block;
                              vertical-align: middle;
                              width: 44%;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="border-radius: 0px; vertical-align: middle"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      font-size: 0px;
                                      padding: 0 0 0 0;
                                      word-break: break-word;
                                    "
                                  >
                                    <div
                                      style="
                                        line-height: 20px;
                                        height: 20px;
                                        mso-line-height-alt: 20px;
                                      "
                                    >
                                      &nbsp;
                                    </div>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    class="img-container"
                                    style="
                                      font-size: 0px;
                                      padding: 0px 0px 0px 26px;
                                      word-break: break-word;
                                      text-align: left;
                                    "
                                  >
                                    <div
                                      style="
                                        margin: 0 auto 0 0;
                                        max-width: 277px;
                                      "
                                    >
                                      <div
                                        class="mktoImg"
                                        id="kimage-5zzg9rkus"
                                        mktolockimgsize="true"
                                        mktolockimgstyle="true"
                                      >
                                        <a
                                          href="https://pixeltests.com/"
                                          target="_blank"
                                          style="
                                            text-decoration: none;
                                            color: #0068a5;
                                          "
                                          ><img
                                            height="auto"
                                            width="277"
                                            src="https://s3-eu-west-1.amazonaws.com/tpd/logos/61321bd12d5b3f001da3d44d/0x0.png"
                                            style="
                                              border: none;
                                              outline: none;
                                              text-decoration: none;
                                              height: auto;
                                              width: 100%;
                                              font-size: 13px;
                                              display: block;
                                            "
                                        /></a>
                                      </div>
                                      <!--[if !mso 9]><!-->
                                      <div
                                        class="mktEditable"
                                        id="image-plain-text-bwib6oa8l"
                                        style="
                                          mso-hide: all;
                                          visibility: hidden;
                                          opacity: 0;
                                          color: transparent;
                                          mso-line-height-rule: exactly;
                                          line-height: 0;
                                          font-size: 0px;
                                          overflow: hidden;
                                          border-width: 0;
                                          display: none !important;
                                        "
                                      >
                                        [ Image ] [[https://pixeltests.com/]]
                                      </div>
                                      <!--<![endif]-->
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          <!--[if mso | IE]></td><td style="vertical-align:middle;width:72px;" ><![endif]-->
                          <div
                            class="mj-column-per-9 mj-outlook-group-fix"
                            style="
                              font-size: 0px;
                              text-align: left;
                              direction: ltr;
                              display: inline-block;
                              vertical-align: middle;
                              width: 9%;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="border-radius: 0px; vertical-align: middle"
                              width="100%"
                            ></table>
                          </div>
                          <div
                            class="mj-column-per-22 mj-outlook-group-fix"
                            style="
                              font-size: 0px;
                              text-align: left;
                              direction: ltr;
                              display: inline-block;
                              vertical-align: middle;
                              width: 22%;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="border-radius: 0px; vertical-align: middle"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      font-size: 0px;
                                      padding: 0 0 0 0;
                                      word-break: break-word;
                                    "
                                  >
                                    <div
                                      style="
                                        line-height: 20px;
                                        height: 20px;
                                        mso-line-height-alt: 20px;
                                      "
                                    >
                                      &nbsp;
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          <!--[if mso | IE]></td><td style="vertical-align:middle;width:200px;" ><![endif]-->
                          <div
                            class="mj-column-per-25 mj-outlook-group-fix"
                            style="
                              font-size: 0px;
                              text-align: left;
                              direction: ltr;
                              display: inline-block;
                              vertical-align: middle;
                              width: 25%;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="border-radius: 0px; vertical-align: middle"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      font-size: 0px;
                                      padding: 0 0 0 0;
                                      word-break: break-word;
                                    "
                                  >
                                    <div
                                      style="
                                        line-height: 20px;
                                        height: 20px;
                                        mso-line-height-alt: 20px;
                                      "
                                    >
                                      &nbsp;
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          <!--[if mso | IE]></td></tr></table><![endif]-->
                        </div>
                        <!--[if mso | IE]></td></tr></table><![endif]-->
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
      <!--[if !mso]><!-->
      <table
        align="center"
        border="0"
        cellpadding="0"
        cellspacing="0"
        role="presentation"
        style="background-color: #f5f5f5; width: 100%"
        class="section"
      >
        <tbody>
          <tr>
            <td align="center">
              <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="hide-on-desktop-outlook block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
              <div
                style="
                  background: #ffffff;
                  background-color: #ffffff;
                  margin: 0px auto;
                  max-width: 800px;
                "
              >
                <table
                  align="center"
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  role="presentation"
                  style="background-color: #ffffff; width: 100%"
                >
                  <tbody>
                    <tr>
                      <td
                        style="
                          display: block;
                          font-size: 0px;
                          padding: 0px 0px 25px 0px;
                          text-align: center;
                          vertical-align: top;
                        "
                        class="hide-on-desktop block-grid"
                        align="center"
                        valign="top"
                      >
                        <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
                        <div
                          class="mj-column-per-100 mj-outlook-group-fix"
                          style="
                            font-size: 0;
                            line-height: 0;
                            text-align: left;
                            display: inline-block;
                            width: 100%;
                            direction: ltr;
                            vertical-align: top;
                          "
                        >
                          <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:440px;" ><![endif]-->
                          <div
                            class="mj-column-per-55 mj-outlook-group-fix"
                            style="
                              font-size: 0px;
                              text-align: left;
                              direction: ltr;
                              display: inline-block;
                              vertical-align: top;
                              width: 55%;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="border-radius: 0px; vertical-align: top"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    class="img-container"
                                    style="
                                      font-size: 0px;
                                      padding: 40px 0px 0px 40px;
                                      word-break: break-word;
                                      text-align: center;
                                    "
                                  >
                                    <div
                                      style="margin: 0 auto; max-width: 400px"
                                      class="img-full-width"
                                    >
                                      <div
                                        class="mktoImg"
                                        id="kimage-7ycymbi9g"
                                        mktolockimgsize="true"
                                        mktolockimgstyle="true"
                                      >
                                        <a
                                          href="https://youtu.be/GGTorJjJq-c?si=Ek3-Jdhv8KSxohvp"
                                          target="_blank"
                                          style="
                                            text-decoration: none;
                                            color: #0068a5;
                                          "
                                          ><img
                                            alt="Meta for Developers"
                                            height="auto"
                                            width="400"
                                            src="http://saipraveen.free.nf/sample/loginissue.png"
                                            style="
                                              border: none;
                                              outline: none;
                                              text-decoration: none;
                                              height: auto;
                                              width: 100%;
                                              font-size: 13px;
                                              display: block;
                                            "
                                        /></a>
                                      </div>
                                      <!--[if !mso 9]><!-->
                                      <div
                                        class="mktEditable"
                                        id="image-plain-text-kwnwbp39k"
                                        style="
                                          mso-hide: all;
                                          visibility: hidden;
                                          opacity: 0;
                                          color: transparent;
                                          mso-line-height-rule: exactly;
                                          line-height: 0;
                                          font-size: 0px;
                                          overflow: hidden;
                                          border-width: 0;
                                          display: none !important;
                                        "
                                      >
                                        [Pixceltest]
                                      </div>
                                      <!--<![endif]-->
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          <!--[if mso | IE]></td><td style="vertical-align:top;width:360px;" ><![endif]-->
                          <div
                            class="mj-column-per-45 mj-outlook-group-fix"
                            style="
                              font-size: 0px;
                              text-align: left;
                              direction: ltr;
                              display: inline-block;
                              vertical-align: top;
                              width: 45%;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="border-radius: 0px; vertical-align: top"
                              width="100%"
                            ></table>
                          </div>
                          <!--[if mso | IE]></td></tr></table><![endif]-->
                        </div>
                        <!--[if mso | IE]></td></tr></table><![endif]-->
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
      <!--<![endif]-->
      <table
        align="center"
        border="0"
        cellpadding="0"
        cellspacing="0"
        role="presentation"
        style="background-color: #f5f5f5; width: 100%"
        class="section"
      >
        <tbody>
          <tr>
            <td align="center">
              <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
              <div
                style="
                  background: #ffffff;
                  background-color: #ffffff;
                  margin: 0px auto;
                  max-width: 800px;
                "
              >
                <table
                  align="center"
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  role="presentation"
                  style="background-color: #ffffff; width: 100%"
                >
                  <tbody>
                    <tr>
                      <td
                        style="
                          font-size: 0px;
                          padding: 0;
                          text-align: center;
                          vertical-align: top;
                        "
                        class="block-grid"
                      >
                        <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td style="vertical-align:top;width:800px;" ><![endif]-->
                        <div
                          class="mj-column-per-100 mj-outlook-group-fix"
                          style="
                            font-size: 0px;
                            text-align: left;
                            direction: ltr;
                            display: inline-block;
                            vertical-align: top;
                            width: 100%;
                          "
                        >
                          <table
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            role="presentation"
                            style="border-radius: 0px; vertical-align: top"
                            width="100%"
                          >
                            <tbody>
                              <tr>
                                <td
                                  class="img-container"
                                  style="
                                    font-size: 0px;
                                    padding: 20px 32px 0px 32px;
                                    word-break: break-word;
                                    text-align: center;
                                  "
                                >
                                  <div style="margin: 0 auto">
                                    <div
                                      class="mktoImg"
                                      id="kimage-84osmwtem"
                                      mktolockimgsize="true"
                                      mktolockimgstyle="true"
                                    >
                                      <a
                                        href="https://youtu.be/GGTorJjJq-c?si=Ek3-Jdhv8KSxohvp"
                                        target="_blank"
                                        style="
                                          text-decoration: none;
                                          color: #0068a5;
                                        "
                                        ><img
                                          height="auto"
                                          width="736"
                                          src="http://saipraveen.free.nf/sample/loginissue.png"
                                          style="
                                            border: none;
                                            outline: none;
                                            text-decoration: none;
                                            height: auto;
                                            width: 100%;
                                            font-size: 13px;
                                            display: block;
                                          "
                                      /></a>
                                    </div>
                                    <!--[if !mso 9]><!-->
                                    <div
                                      class="mktEditable"
                                      id="image-plain-text-uwpi6n79z"
                                      style="
                                        mso-hide: all;
                                        visibility: hidden;
                                        opacity: 0;
                                        color: transparent;
                                        mso-line-height-rule: exactly;
                                        line-height: 0;
                                        font-size: 0px;
                                        overflow: hidden;
                                        border-width: 0;
                                        display: none !important;
                                      "
                                    >
                                      [ Pixeltest ] [[https://pixeltests.com/]]
                                    </div>
                                    <!--<![endif]-->
                                  </div>
                                </td>
                              </tr>
                              <tr>
                                <td
                                  class="text-container"
                                  style="
                                    font-size: 0px;
                                    padding: 26px 32px 0px 32px;
                                    word-break: break-word;
                                    text-align: left;
                                  "
                                >
                                  <div
                                    class="mktEditable"
                                    id="ktext-i3zp9uvdr"
                                    style="
                                      font-family: 'Optimistic Text', Helvetica,
                                        sans-serif;
                                      font-size: 16px;
                                      letter-spacing: none;
                                      line-height: 1.8;
                                      text-align: left;
                                      mso-line-height-alt: 1.813em;
                                      color: #414141;
                                    "
                                  >
                                    <div class="links-0068A5-underline">
                                      <div
                                        style="
                                          font-family: 'Optimistic Text',
                                            Helvetica, sans-serif;
                                          font-size: 16px;
                                          letter-spacing: none;
                                          line-height: 1.8;
                                          text-align: left;
                                          mso-line-height-alt: 1.813em;
                                          color: #414141;
                                        "
                                      >
                                        <p style="margin: 0 0">
                                          <em
                                            >“We sincerely apologize for any inconvenience you may have experienced. Your satisfaction is our top priority, and we regret that we fell short of meeting your expectations.

                                            Please rest assured that we are actively working to resolve the issue you've encountered. Our team is dedicated to providing prompt and effective assistance to address your concerns. please follow these steeps   ”
                                            &nbsp;</em
                                          ><br />
                                          <!-- <em
                                            >-Kevin Carson, SVP Global Artist
                                            and Industry Relations at Smule</em
                                          > -->
                                        </p>
                                        <!-- <p style="margin: 0 0">&nbsp;</p>
                                        <p style="margin: 0 0">
                                          Enabling
                                          <a
                                            href="https://content.atmeta.com/n/MjY3LVBWQi05NDEAAAGPMB9ddtadOfb4B6_Z68ee3OBpJZHQb6xK1YP982oND43OPCSrJ0AOwDFdgBp7Dy_5QSRo7hw="
                                            target="_blank"
                                            rel="noopener"
                                            style="
                                              color: rgb(0, 104, 165);
                                              text-decoration: underline;
                                            "
                                            >Sharing to Reels</a
                                          >
                                          makes it easy for people to share
                                          short-form videos directly to
                                          Instagram Reels from your app, where
                                          they can reach a wider audience and
                                          increase awareness of your app at the
                                          same time.&nbsp;
                                        </p> -->
                                        <p style="margin: 0 0">&nbsp;</p>
                                        <p style="margin: 0 0">
                                          <strong
                                            >please follow these steps</strong
                                          >
                                        </p>
                                        <ul
                                          style="
                                            display: block;
                                            margin-top: 0;
                                            margin-bottom: 0;
                                            padding-left: 40px;
                                            mso-para-margin-left: 40px;
                                          "
                                        >
                                          {samplevariable}
                                        </ul>
                                        <p style="margin: 0 0">&nbsp;</p>
                                        <p style="margin: 0 0">
                                          <strong
                                            >Are you satisifed with this solutation?&nbsp;</strong
                                          ><br/>If you satisifed with this solutation please click on the Yes button and if you are not satisifed with this solutation please click on the No button
                                        </p>
                                        <p style="margin: 0 0">&nbsp;</p>
                                      </div>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <table
        align="center"
        border="0"
        cellpadding="0"
        cellspacing="0"
        role="presentation"
        style="background-color: #f5f5f5; width: 100%"
        class="section"
      >
        <tbody>
          <tr>
            <td align="center">
              <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="block-grid-outlook" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
              <div
                style="
                  background: #ffffff;
                  background-color: #ffffff;
                  margin: 0px auto;
                  max-width: 800px;
                "
              >
                <table
                  align="center"
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  role="presentation"
                  style="background-color: #ffffff; width: 100%"
                >
                  <tbody>
                    <tr>
                      <td
                        style="
                          font-size: 0px;
                          padding: 0px;
                          text-align: center;
                          vertical-align: top;
                        "
                        class="block-grid"
                      >
                        <div
                          class="mj-column-per-50 mj-outlook-group-fix"
                          style="
                            font-size: 0px;
                            text-align: left;
                            direction: ltr;
                            display: inline-block;
                            vertical-align: top;
                            width: 100%;
                          "
                        >
                          <table
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            role="presentation"
                            style="border-radius: 0px; vertical-align: top"
                            width="100%"
                          >
                            <tbody>
                              <tr>
                                <td
                                  valign="middle"
                                  class="button-container"
                                  style="
                                    font-size: 0px;
                                    padding: 10px 25px 10px 25px;
                                    word-break: break-word;
                                    text-align: center;
                                  "
                                >
                                  <div>
                                    <a
                                      href="Solved Link"
                                      style="
                                        display: inline-block;
                                        background: #ffffff;
                                        color: #000000;
                                        font-family: 'Optimistic Text',
                                          Helvetica, sans-serif;
                                        font-size: 16px;
                                        font-weight: bold;
                                        line-height: 1;
                                        margin: 0;
                                        text-align: center;
                                        text-decoration: none;
                                        text-transform: none;
                                        padding: 10px 25px 10px 25px;
                                        mso-padding-alt: 0px;
                                        border-radius: 25px;
                                        border-left: 1px solid #000000;
                                        border-right: 1px solid #000000;
                                        border-top: 1px solid #000000;
                                        border-bottom: 1px solid #000000;
                                        mso-border-alt: none;
                                        box-sizing: border-box;
                                      "
                                      target="_blank"
                                      width="80"
                                      ><strong>Yes Solved</strong>
                                    </a>
                                    <div
                                      class="mktEditable"
                                      id="button-plain-text-pogk2gcmj"
                                      style="
                                        mso-hide: all;
                                        visibility: hidden;
                                        opacity: 0;
                                        color: transparent;
                                        mso-line-height-rule: exactly;
                                        line-height: 0;
                                        font-size: 0px;
                                        overflow: hidden;
                                        border-width: 0;
                                        display: none !important;
                                      "
                                    >
                                      Yes Solved
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                        <div
                          class="mj-column-per-50 mj-outlook-group-fix"
                          style="
                            font-size: 0px;
                            text-align: left;
                            direction: ltr;
                            display: inline-block;
                            vertical-align: top;
                            width: 100%;
                          "
                        >
                          <table
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            role="presentation"
                            style="border-radius: 0px; vertical-align: top"
                            width="100%"
                          >
                            <tbody>
                              <tr>
                                <td
                                  valign="middle"
                                  class="button-container"
                                  style="
                                    font-size: 0px;
                                    padding: 10px 25px 10px 25px;
                                    word-break: break-word;
                                    text-align: center;
                                  "
                                >
                                  <div>
                                    <a
                                      href="Unsolved Link"
                                      style="
                                        display: inline-block;
                                        background: #ffffff;
                                        color: #000000;
                                        font-family: 'Optimistic Text',
                                          Helvetica, sans-serif;
                                        font-size: 16px;
                                        font-weight: bold;
                                        line-height: 1;
                                        margin: 0;
                                        text-align: center;
                                        text-decoration: none;
                                        text-transform: none;
                                        padding: 10px 25px 10px 25px;
                                        mso-padding-alt: 0px;
                                        border-radius: 25px;
                                        border-left: 1px solid #000000;
                                        border-right: 1px solid #000000;
                                        border-top: 1px solid #000000;
                                        border-bottom: 1px solid #000000;
                                        mso-border-alt: none;
                                        box-sizing: border-box;
                                      "
                                      target="_blank"
                                      width="114"
                                      ><strong>Not Solved</strong>
                                    </a>
                                    <div
                                      class="mktEditable"
                                      id="button-plain-text-kcixzgmz8"
                                      style="
                                        mso-hide: all;
                                        visibility: hidden;
                                        opacity: 0;
                                        color: transparent;
                                        mso-line-height-rule: exactly;
                                        line-height: 0;
                                        font-size: 0px;
                                        overflow: hidden;
                                        border-width: 0;
                                        display: none !important;
                                      "
                                    >
                                      Yes Solved
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      
    </div>
    
  </body>
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
        
