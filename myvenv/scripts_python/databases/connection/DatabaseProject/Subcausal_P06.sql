IF OBJECT_ID('[dbo].[Subcausal_P06_]', 'U') IS NOT NULL
DROP TABLE [dbo].[Subcausal_P06_]
GO

CREATE TABLE Subcausal_P06_(
    id INT PRIMARY KEY,
    codigo NVARCHAR(6),
    descripcion NVARCHAR(255)
);

INSERT INTO Subcausal_P06_ (id, codigo, descripcion)
VALUES
    (1, N'P06_1', N'Solicitud de pago a tercero autorizado por fallecimiento del cotizante'
    );
GO