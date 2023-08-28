IF OBJECT_ID('[dbo].[Subcausal_P05_]', 'U') IS NOT NULL
DROP TABLE [dbo].[Subcausal_P05_]
GO

CREATE TABLE Subcausal_P05_(
    id INT PRIMARY KEY,
    codigo NVARCHAR(6),
    descripcion NVARCHAR(255)
);

INSERT INTO Subcausal_P05_ (id, codigo, descripcion)
VALUES
    (1, N'P05_1', N'Aportante dependiente realiza solicitud de pago por proceso normal y radica PQRS'),
    (2, N'P05_2', N'Aportante independiente realiza solicitud de pago por proceso normal y radica PQRS');

GO