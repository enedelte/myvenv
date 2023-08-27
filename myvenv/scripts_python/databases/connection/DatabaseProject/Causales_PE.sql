-- Create a new table called '[Causales_PE]' in schema '[dbo]'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[Causales_PE]', 'U') IS NOT NULL
DROP TABLE [dbo].[Causales_PE]
GO
-- Create the table in the specified schema
CREATE TABLE Causales_PE (
    id INT PRIMARY KEY,
    codigo NVARCHAR(3),
    descripcion NVARCHAR(255)
);

INSERT INTO Causales_PE (id, codigo, descripcion)
VALUES
    (1, N'P01', N'Solicitud de Pago inicial'),
    (2, N'P02', N'Correccion origen y/o datos de la incapacidad'),
    (3, N'P03', N'Solicitud de informacion tramites pago y transcripcion'),
    (4, N'P04', N'Solicitud de incapacidad y/o licencia con pago ya autorizado'),
    (5, N'P05', N'Solicitud de incapacidad en proceso de autorizacion menor a 15 días'),
    (6, N'P06', N'Solicitud de pago a tercero autorizado por fallecimiento del cotizante'),
    (7, N'P07', N'Solicitud de retoma de Incapacidad y/o licencia por negacion anterior'),
    (8, N'P08', N'Solicitud de Reliquidacion y/o ajuste en el valor liquidado'),
    (9, N'P09', N'Mala atencion de OAA no radican solicitud de pago'),
    (10, N'P10', N'Solicitud de pago de Incapacidad Inferior a 3 Días'),
    (11, N'P11', N'Solicitud de pago de incapacidades mayores a 180 días'),
    (12, N'P12', N'Solicitud de pago de incapacidades mayores a 540 días'),
    (13, N'P13', N'Solicitud de aclaracion de pago de incapacidades'),
    (14, N'P14', N'Solicitud de certificado detallado de incapacidades'),
    (15, N'P15', N'Usuario asignacion (Incapacidad Generada en EPS anterior)'),
    (16, N'P16', N'Solicitud pago de incapacidad AT o EP'),
    (17, N'P17', N'Incapacidad perdio vigencia para cobro'),
    (18, N'P18', N'Solicitud de aclaracion de negacion de pago'),
    (19, N'P19', N'Solicitud de pago de incapacidades reconocidas por tracto sucesivo-tutela'),
    (20, N'P20', N'Solicitud de reconocimiento por cumpliento de fallos de tutela'),
    (21, N'P21', N'Solicitud de Aportante masivo'),
    (22, N'P22', N'Información solicitud no es queja');
GO