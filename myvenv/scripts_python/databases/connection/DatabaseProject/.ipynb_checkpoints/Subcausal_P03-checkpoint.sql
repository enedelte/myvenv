IF OBJECT_ID('[dbo].[Subcausal_P03_]', 'U') IS NOT NULL
DROP TABLE [dbo].[Subcausal_P03_]
GO

CREATE TABLE Subcausal_P03_(
    id INT PRIMARY KEY,
    codigo NVARCHAR(6),
    descripcion NVARCHAR(255)
);

INSERT INTO Subcausal_P03_ (id, codigo, descripcion)
VALUES
    (1, N'P03_1', N'Requiere información para tramitar licencia compartida y/o Flexible Ley 2114 de 2021'),
    (2, N'P03_2', N'Requiere información Decreto 1427 de 2022'),
    (3, N'P03_3', N'Requiere información de creación de cuenta remite documentos'),
    (4, N'P03_4', N'Requiere información del tramite para solicitar el pago de incapacidades'),
    (5, N'P03_5', N'Requiere información cambio de cuenta bancaria por embargo'),
    (6, N'P03_6', N'Requiere información del tramite para el pago de una incapacidad mayor a 540 días');

GO