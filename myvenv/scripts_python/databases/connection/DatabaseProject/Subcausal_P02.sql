IF OBJECT_ID('[dbo].[Subcausal_P02_]', 'U') IS NOT NULL
DROP TABLE [dbo].[Subcausal_P02_]
GO

CREATE TABLE Subcausal_P02_(
    id INT PRIMARY KEY,
    codigo NVARCHAR(6),
    descripcion NVARCHAR(255)
);

INSERT INTO Subcausal_P02_ (id, codigo, descripcion)
VALUES
    (1, N'P02_1', N'Solicita cambio de origen (nuevo dictamen)'),
    (2, N'P02_2', N'Solicita modificar días de la incapacidad (error en transcripción) ajuste en pago'),
    (3, N'P02_3', N'Solicita modificar datos de la incapacidad por error en la transcripción'),
    (4, N'P02_4', N'Solicita modificar datos de la incapacidad no es procedente'),
    (5, N'P02_5', N'Solicita ajustar la prórroga de incapacidades expedidas y ajustar conteo');

GO


