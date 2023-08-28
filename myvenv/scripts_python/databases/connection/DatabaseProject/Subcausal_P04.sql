IF OBJECT_ID('[dbo].[Subcausal_P04_]', 'U') IS NOT NULL
DROP TABLE [dbo].[Subcausal_P04_]
GO

CREATE TABLE Subcausal_P04_(
    id INT PRIMARY KEY,
    codigo NVARCHAR(6),
    descripcion NVARCHAR(255)
);

INSERT INTO Subcausal_P04_ (id, codigo, descripcion)
VALUES
    (1, N'P04_1', N'Solicitud pago de incapacidad autorizada con más de 5 días hábiles'),
    (2, N'P04_2', N'Solicitud pago de incapacidad autorizada con menos de 5 días hábiles'),
    (3, N'P04_3', N'Solicitud pago de licencia autorizada con más de 5 días hábiles'),
    (4, N'P04_4', N'Solicitud pago de licencia autorizada con menos de 5 días hábiles');

GO