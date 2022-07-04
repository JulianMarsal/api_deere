/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const getBoundary = /* GraphQL */ `
  query GetBoundary($organizationId: ID!, $fieldId: String!) {
    getBoundary(organizationId: $organizationId, fieldId: $fieldId) {
      type
      name
      sourceType
      createdTime
      modifiedTime
      area {
        type
        valueAsDouble
        unit
      }
      workableArea {
        type
        valueAsDouble
        unit
      }
      multipolygons {
        type
      }
      extent {
        type
      }
      archived
      id
      active
      irrigated
    }
  }
`;
export const listFields = /* GraphQL */ `
  query ListFields($organizationId: ID) {
    listFields(organizationId: $organizationId) {
      type
      name
      archived
      id
      links {
        rel
        uri
      }
    }
  }
`;
export const listClients = /* GraphQL */ `
  query ListClients($organizationId: ID!) {
    listClients(organizationId: $organizationId) {
      name
      links {
        rel
        uri
      }
      id
      archived
    }
  }
`;
