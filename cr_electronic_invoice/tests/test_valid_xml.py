import unittest
from lxml import etree
from xmltest import XMLAssertions
from lxml.doctestcompare import PARSE_XML, LXMLOutputChecker
from lxml.etree import XMLSyntaxError


class ContextCRTestCase(unittest.TestCase, XMLAssertions):

    def assertXmlDocument(self, data):
        """Asserts `data` is an XML document and returns it.
        Assertion and XML parsing using lxml.
        """
        # no assertion yet
        try:
            doc = etree.fromstring(data)
        except XMLSyntaxError as e:
            raise self.fail('Input is not a valid XML document: %s' % e)

        return doc

    def test_valid_xml(self):
        # write exactly the same test as in previous example

        data = """<?xml version='1.0'?>
        <FacturaElectronica xmlns="https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.3/facturaElectronica" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://www.hacienda.go.cr/ATV/ComprobanteElectronico/docs/esquemas/2016/v4.3/FacturaElectronica_V4.3.xsd"><Clave>50625072000010679062900100001010000000051129408402</Clave><CodigoActividad>749302</CodigoActividad><NumeroConsecutivo>00100001010000000051</NumeroConsecutivo><FechaEmision>2020-07-25T22:34:34-06:00</FechaEmision><Emisor><Nombre>EUGENIA EMERITA DE LA TRINIDAD HERNANDEZ AGUERO</Nombre><Identificacion><Tipo>01</Tipo><Numero>106790629</Numero></Identificacion><NombreComercial>Multiservicios EUH</NombreComercial><Ubicacion><Provincia>1</Provincia><Canton>07</Canton><Distrito>01</Distrito><Barrio>08</Barrio><OtrasSenas>Barrio San Bosco</OtrasSenas></Ubicacion><Telefono><CodigoPais>506</CodigoPais><NumTelefono>88980968</NumTelefono></Telefono><CorreoElectronico>jhulloahernandez@gmail.com</CorreoElectronico></Emisor><Receptor><Nombre>JASON DE LA TRINIDAD ULLOA HERNANDEZ</Nombre><Identificacion><Tipo>01</Tipo><Numero>113040714</Numero></Identificacion><Ubicacion><Provincia>1</Provincia><Canton>07</Canton><Distrito>01</Distrito><Barrio>08</Barrio><OtrasSenas>Barrio San Bosco</OtrasSenas></Ubicacion><Telefono><CodigoPais>506</CodigoPais><NumTelefono>88980968</NumTelefono></Telefono><CorreoElectronico>jhulloahernandez@gmail.com</CorreoElectronico></Receptor><CondicionVenta>01</CondicionVenta><PlazoCredito>0</PlazoCredito><MedioPago>01</MedioPago><DetalleServicio><LineaDetalle><NumeroLinea>1</NumeroLinea><CodigoComercial><Tipo>04</Tipo><Codigo>500</Codigo></CodigoComercial><Cantidad>1.0</Cantidad><UnidadMedida>Unid</UnidadMedida><Detalle>[500] Disco Duro</Detalle><PrecioUnitario>6000.0</PrecioUnitario><MontoTotal>6000.0</MontoTotal><SubTotal>6000.0</SubTotal><Impuesto><Codigo>01</Codigo><CodigoTarifa>08</CodigoTarifa><Tarifa>13.0</Tarifa><Monto>780.0</Monto></Impuesto><ImpuestoNeto>780.0</ImpuestoNeto><MontoTotalLinea>6780.0</MontoTotalLinea></LineaDetalle></DetalleServicio><ResumenFactura><CodigoTipoMoneda><CodigoMoneda>CRC</CodigoMoneda><TipoCambio>1.0</TipoCambio></CodigoTipoMoneda><TotalServGravados>0.0</TotalServGravados><TotalServExentos>0.0</TotalServExentos><TotalServExonerado>0.0</TotalServExonerado><TotalMercanciasGravadas>6000.0</TotalMercanciasGravadas><TotalMercanciasExentas>0.0</TotalMercanciasExentas><TotalMercExonerada>0.0</TotalMercExonerada><TotalGravado>6000.0</TotalGravado><TotalExento>0.0</TotalExento><TotalExonerado>0.0</TotalExonerado><TotalVenta>6000.0</TotalVenta><TotalDescuentos>0.0</TotalDescuentos><TotalVentaNeta>6000.0</TotalVentaNeta><TotalImpuesto>780.0</TotalImpuesto><TotalOtrosCargos>0.0</TotalOtrosCargos><TotalComprobante>6780.0</TotalComprobante></ResumenFactura><ds:Signature Id="Signature-2147">
        <ds:SignedInfo>
        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
        <ds:Reference Id="Reference-2292" URI="">
        <ds:Transforms>
        <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue>InsUvfORfv5CGeOO/gHgLzuYZvRezh0EQgMsRpggEmE=</ds:DigestValue>
        </ds:Reference>
        <ds:Reference Id="ReferenceKeyInfo" URI="#KeyInfoId-Signature-2147">
        <ds:Transforms>
        <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue>SlfT0G7e75Dd+f7r58OiNoPmKHCI5kSKmXnIHHsbo5E=</ds:DigestValue>
        </ds:Reference>
        <ds:Reference URI="#SignedProperties-Signature-2147" Type="http://uri.etsi.org/01903#SignedProperties">
        <ds:Transforms>
        <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue>Wac/DlnMPkMeyIT4wGQKeExhOWSmNyOIzgxsZS/5Kzk=</ds:DigestValue>
        </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue>eXKzATEiwkHsn8r3k+xFAhFJg6f9dFekrgdzYUGxWgKc9spehaqIR7LI2v0CBT/jc/F41vtqeVtIkz+o69bE9yzN9yV6wW6ofwfth59O7IB7iaRgoRBHdt0CpbMTG4VFzaRGg9V/NO0hncWEPwz2VpkK5jSmeDE7gDlb08dI/S+ApL3EQnwrSoWRcMtO01uzH7BcobdEWA/xItzETp4dHG1caPjX5LOpKx7Ic5+qzGc9lHNugHfLq82ZE4OjytB8b2u9eb/KHu+xhJpQfuAg+ijQ0ejF0puIjobeWwpSLgKW6DYuVYNx58qXeRRAAAqb6ZFUyQEZky6tsxCZUbX94A==</ds:SignatureValue>
        <ds:KeyInfo Id="KeyInfoId-Signature-2147">
        <ds:X509Data>
        <ds:X509Certificate>MIIFhTCCA22gAwIBAgIGAXExWpE0MA0GCSqGSIb3DQEBCwUAMGwxCzAJBgNVBAYTAkNSMSkwJwYDVQQKDCBNSU5JU1RFUklPIERFIEhBQ0lFTkRBIC0gU0FOREJPWDEMMAoGA1UECwwDREdUMSQwIgYDVQQDDBtDQSBQRVJTT05BIEZJU0lDQSAtIFNBTkRCT1gwHhcNMjAwMzMxMTYwOTExWhcNMjIwMzMxMTYwOTExWjCBzTEZMBcGA1UEBRMQQ1BGLTAxLTA2NzktMDYyOTEZMBcGA1UEBAwQSEVSTkFOREVaIEFHVUVSTzEnMCUGA1UEKgweRVVHRU5JQSBFTUVSSVRBIERFIExBIFRSSU5JREFEMQswCQYDVQQGEwJDUjEXMBUGA1UECgwOUEVSU09OQSBGSVNJQ0ExDDAKBgNVBAsMA0NQRjE4MDYGA1UEAwwvRVVHRU5JQSBFTUVSSVRBIERFIExBIFRSSU5JREFEIEhFUk5BTkRFWiBBR1VFUk8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCH6sfZilXoDbcBcsFXa+IpC+bPvRQqXPFN8QzQnpgxtKQMB8bxMBsBzaTddyLLOFcnU3Hg64XzYSUZV87PPeQwU6TuxcI1GWfcMDH12L9HonJonm5xdv0WoOYBSMUbST7bA8IReKEmtD7nu1ywmYiDBSrx+RYV5lqg28WUVQMVPyt/GTTQPJsRyLvYIVWRxNpjzSPC/nhhaPhxbX9IY6i3gxEHmnvMgetO8UYPfCxOtBOw3Y9SNJ0rNkRJW5mjRjQnU4t6H2UUgcovwraFHXGrguozDLOS2VFjYK0LnvssbUuAr6H3ujv/k50e507iyg2a3pUYTBQ6gfed+Qkad5K9AgMBAAGjgcowgccwHwYDVR0jBBgwFoAURiPSRE+/V1kh5L+T1TCblUzj94cwHQYDVR0OBBYEFLZbJbKCCBoAVxt+cj1CCb/Qi5JcMAsGA1UdDwQEAwIGwDATBgNVHSUEDDAKBggrBgEFBQcDBDBjBggrBgEFBQcBAQRXMFUwUwYIKwYBBQUHMAKGR2h0dHBzOi8vcGtpLmNvbXByb2JhbnRlc2VsZWN0cm9uaWNvcy5nby5jci9zdGFnL2ludGVybWVkaWF0ZS1wZi1wZW0uY3J0MA0GCSqGSIb3DQEBCwUAA4ICAQBq1G8qnQrIv253wjHjm06/FizZDq/IUV6W0ne7tCuEu49XldnjChPyfPmy3r84ntORaU3R3wFekmyNAv3pzKNxAenLBKscFvQKNJ5/Lm3XgCQhCfMLhQQABv2WHPLL/+qH4Y2IRvuSjf1D31fNJgqa5jXxWYTicl0eJEpUSXqRlfr/s++EEAwvjFMrjx6wq8fUXfM6xg1YprOObcO+UKfVaxDe3HbahnFudbGdYec7U3/8pPmMAugRJrXNNuoAu0epxz2yBrp7NIzzyQN33QQq9UmbWXVga+WjN4s+peNENFDX5x/kHB/3zY7DyfOd2XI+LmF10oANGV7gGZxcFymHNDIvuorQXe8DDCFSUB5f9IAm/AEW3U82dXHME1FEwfgf/ZhV8+gOeie+lshV3GY6Z9gZPTpABm4kjYXpjP4PeLkDGPVbtQEAD/5BBtQwWNLR1U846UGQ/EjM8MqQwi1LzPF0LHFMBdw/lBwPZgO3ZPk6AtJAKeFNLUfYdICEikfANC/vrKTOLM1b3qoquXayqd2revuREdBi+FYCCHslsiyztrpAXx0Un0iL36MnZ+Pbw1zqYm7HQh3L7GltPRnnatm0HJCOPyRSZvu7mRD2WUKe44rxDY9sfj4rPZboDdJziBhUYe0j3YgkY8TmdjPqI+9T3ejJZYD3MtqI2eE3tg==</ds:X509Certificate>
        </ds:X509Data>
        <ds:KeyValue>
        <ds:RSAKeyValue>
        <ds:Modulus>h+rH2YpV6A23AXLBV2viKQvmz70UKlzxTfEM0J6YMbSkDAfG8TAbAc2k3XciyzhXJ1Nx4OuF82ElGVfOzz3kMFOk7sXCNRln3DAx9di/R6JyaJ5ucXb9FqDmAUjFG0k+2wPCEXihJrQ+57tcsJmIgwUq8fkWFeZaoNvFlFUDFT8rfxk00DybEci72CFVkcTaY80jwv54YWj4cW1/SGOot4MRB5p7zIHrTvFGD3wsTrQTsN2PUjSdKzZESVuZo0Y0J1OLeh9lFIHKL8K2hR1xq4LqMwyzktlRY2CtC577LG1LgK+h97o7/5OdHudO4soNmt6VGEwUOoH3nfkJGneSvQ==</ds:Modulus>
        <ds:Exponent>AQAB</ds:Exponent>
        </ds:RSAKeyValue>
        </ds:KeyValue>
        </ds:KeyInfo>
        <ds:Object><xades:QualifyingProperties xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" Target="#Signature-2147" Id="XadesObjects"><xades:SignedProperties Id="SignedProperties-Signature-2147"><xades:SignedSignatureProperties><xades:SigningTime>2020-07-26T04:33:40.146769+00:00</xades:SigningTime><xades:SigningCertificate><xades:Cert><xades:CertDigest><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>3wO8LujeZXaNz/S4z9TbNrFXJbA=</ds:DigestValue></xades:CertDigest><xades:IssuerSerial><ds:X509IssuerName>CN=CA PERSONA FISICA - SANDBOX,OU=DGT,O=MINISTERIO DE HACIENDA - SANDBOX,C=CR</ds:X509IssuerName><ds:X509SerialNumber>1585670951220</ds:X509SerialNumber></xades:IssuerSerial></xades:Cert></xades:SigningCertificate><xades:SignaturePolicyIdentifier><xades:SignaturePolicyId><xades:SigPolicyId><xades:Identifier>https://www.hacienda.go.cr/ATV/ComprobanteElectronico/docs/esquemas/2016/v4.2/ResolucionComprobantesElectronicosDGT-R-48-2016_4.2.pdf</xades:Identifier><xades:Description/></xades:SigPolicyId><xades:SigPolicyHash><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>E9/BBP0G1Z3JJQzOpwqpJuf7xdY=</ds:DigestValue></xades:SigPolicyHash></xades:SignaturePolicyId></xades:SignaturePolicyIdentifier></xades:SignedSignatureProperties><xades:SignedDataObjectProperties><xades:DataObjectFormat ObjectReference="#Reference-2292"><xades:MimeType>text/xml</xades:MimeType><xades:Encoding>UTF-8</xades:Encoding></xades:DataObjectFormat></xades:SignedDataObjectProperties></xades:SignedProperties></xades:QualifyingProperties></ds:Object></ds:Signature></FacturaElectronica>
        """

        self.assertXmlDocument(data)
