IF OBJECT_ID('[dbo].[Subcausal_P01]', 'U') IS NOT NULL
DROP TABLE [dbo].[Subcausal_P01_]
GO

CREATE TABLE Subcausal_P01(
    id INT PRIMARY KEY,
    codigo NVARCHAR(6),
    descripcion NVARCHAR(255)
);

INSERT INTO Subcausal_P01 (id, codigo, descripcion)
VALUES
    (1, N'P01_1', N'Solicitud de Pago inicial que no se logró realizar por Portal'),
    (2, N'P01_2', N'Solicitud de pago que no registra (aportante informa radicar solicitud)'),
    (3, N'P01_3', N'Aportante presenta problemas con portal'),
    (4, N'P01_4', N'Solicitud de pago radicada en OAA no hay PDA ni ON-BASE'),
    (5, N'P01_5', N'Solicitud de transcripción no se realizó solicitud de pago');

GO



